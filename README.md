# Spotify-Playlist-Downloader
Simple script to download all the songs present in a Spotify playlist in mp3 format

- Installing dependancies:
  Keep the requirements.txt file in the root folder of your project and execute the following code:
  ``` pip install -r requirements.txt```
  
- Create Spotify API Key and Secret Key by creating a new app [here](https://developer.spotify.com/dashboard/login).
  Now set both the keys as environement variables 
  
- If you are on windows, download and extract the ffmpeg-build.zip file present in repo. 
  Extract it and go in the bin folder inside ffmpeg folder, copy the path and set this path in the system variable named path. 

- For running the script, only the URI of the playlist is needed. To get it, go to your spotify playlist, 
  click the three dots->Share->Copy Spotify URI
  From the URI, copy the whole string after spotify:playlist:
  For example, if the playlist URI is spotify:playlist:1p6Qapm1UAUBHqDp3uSSKn, copy 1p6Qapm1UAUBHqDp3uSSKn and run the script as shown below:
  ``` python main.py "1p6Qapm1UAUBHqDp3uSSKn" ```
  
- If during song download process, the process terminates due to some issue, just re-run the script and everything will be fine. 
  
