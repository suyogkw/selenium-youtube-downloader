# selenium-youtube-downloader
A selenium based python script to download youtube music files. using rg3/youtube-dl.
thanks to rg3/youtube-dl.
thanks to selenium python.

There are two python scripts in the repository.

1) ytd_searchdownload.py
  
  This script can be used for downloading youtube songs in a folder structure
  with album name as folder and all songs inside it.
  Basically, the program will search youtube.com for search strings provided
  in input file added with album name, download the first search result in album folder.
  
  input file : searchdownload.txt
  input example -> 
  Prateek Kuhad : Dil Beparwah
  this will search youtube for 'Dil Beparwah Prateek Kuhad' and download top result to folder 'Prateek Kuhad'
 
2) ytd_topsuggestion.py
  
  This script can be used for downloading youtube top song suggestion playlist in a folder structure
  with album name as folder and all songs inside it.
  The program will search youtube.com for search strings provided
  in input file, download the first search result then make use of youtube's top suggestion and go on downloading
  the songs for specified number of songs.
  
  Results are found to be better with youtube logged in, hence logging in script is also added.
  
  input file : topsuggestion.txt
  input example -> 
  5 : Coldplay
  this will search youtube for 'Coldplay' and download top result to folder 'Coldplay'
  then download the next top suggestion and next top suggestion and so on for 5 times.
