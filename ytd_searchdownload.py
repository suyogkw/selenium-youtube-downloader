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

#read search strings from file
search_strings = []
with open('./searchdownload.txt') as f:
     search_strings = { k.strip():v.strip() for line in f for (v, k) in (line.strip().split(':', 1),)}

#go one by one through the search strings
for key in search_strings:
    song_name = key
    album_name = search_strings[key]
    #create folder with albumname
    if not os.path.exists('Downloads/'+album_name):
        os.makedirs('Downloads/'+album_name)
    
    outputDir = './Downloads/'+album_name+'/'+'%(title)s.%(ext)s'
    ydl_opts = {'format': 'bestaudio/best',
        'outtmpl': outputDir}

    #search
    fld_input = wait.until(EC.element_to_be_clickable((By.NAME, 'search_query')))
    fld_input.clear()
    fld_input.send_keys(song_name+' '+album_name)
    time.sleep(1)
    fld_input.send_keys(Keys.ENTER)
        
    #download songs
    driver.get(driver.current_url)
    thumbnail = wait.until(EC.element_to_be_clickable((By.ID, 'thumbnail')))
    song_url = thumbnail.get_attribute('href')
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([song_url])