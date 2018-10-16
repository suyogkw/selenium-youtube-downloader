from __future__ import unicode_literals
import youtube_dl
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

#initialize headless driver
chrome_options = Options()
chrome_options.add_argument("--disable-notifications")
#chrome_options.add_argument("--headless")
driver = webdriver.Chrome(executable_path='./chrome/chromedriver.exe',   chrome_options=chrome_options) 
wait = WebDriverWait(driver, 10)


driver.get('https://www.youtube.com/')
driver.maximize_window()

#signing in
sign_in = wait.until(EC.element_to_be_clickable((By.ID, 'text')))
sign_in.click()

credentials = []
with open('./credentials.txt') as f:
    credentials = [line.strip() for line in f]

usrname = credentials[0]
password = credentials[1]

fld_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="email"]')))
fld_input.send_keys(usrname)

btn_next = wait.until(EC.element_to_be_clickable((By.ID, 'identifierNext')))
btn_next.click()

fld_input = wait.until(EC.element_to_be_clickable((By.XPATH, '//input[@type="password"]')))
fld_input.send_keys(password)

btn_next = wait.until(EC.element_to_be_clickable((By.ID, 'passwordNext')))
btn_next.click()

#read search strings from file
search_strings = []
with open('./topsuggestion.txt') as f:
     search_strings = { k.strip():int(v) for line in f for (v, k) in (line.strip().split(':', 1),)}

#go one by one through the search strings
for key in search_strings:
    albumname=key
    #create folder with albumname
    if not os.path.exists('Downloads/'+albumname):
        os.makedirs('Downloads/'+albumname)
    
    outputDir = './Downloads/'+albumname+'/'+'%(title)s.%(ext)s'
    ydl_opts = {'format': 'bestaudio/best',
        'outtmpl': outputDir}

    #search
    fld_input = wait.until(EC.element_to_be_clickable((By.ID, 'search')))
    fld_input.send_keys(albumname)
    time.sleep(1)
    fld_input.send_keys(Keys.ENTER)
        
    #songs
    for item in range(search_strings[albumname]):
        #get top suggestion
        driver.get(driver.current_url)
        thumbnail = wait.until(EC.element_to_be_clickable((By.ID, 'thumbnail')))
        song_url = thumbnail.get_attribute('href')
        thumbnail.click()
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([song_url])
        
        