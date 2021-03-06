import youtube_dl
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from youtube_search import YoutubeSearch
import time
import sys


#Spotify Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=os.environ.get('SPOTIFY_CLIENT_ID'),
                                              client_secret=os.environ.get('SPOTIFY_CLIENT_SECRET'),
                                              redirect_uri="http://example.com/",
                                              scope="playlist-read-private",
                                               ))
#Youtube Downloader Arguments
ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '320',
    }],
}

#Getting the playlist details
playlist = sp.playlist_items(playlist_id=sys.argv[1])

#Main
for key in playlist['items']:
    track_name = key['track']['name']
    artist_name = key['track']['artists'][0]['name']
    results = YoutubeSearch(f'{artist_name} {track_name}', max_results=2).to_dict()
    get_id=results[0]['id']
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([f'https://www.youtube.com/watch?v={get_id}'])
    time.sleep(1)


