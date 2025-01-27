import json
import requests
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")
playlist_id = os.getenv("SPOTIFY_PLAYLIST_ID")


def get_token():
    
    url = "https://accounts.spotify.com/api/token"  

    payload = {
        "grant_type": "client_credentials",
        "client_id": client_id,        
        "client_secret": client_secret 
    }

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        resp_json = response.json()
    
    return resp_json['access_token']

        
def get_playlist():

    ACCESS_TOKEN = get_token()

    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    headers = {
        "Authorization": f'Bearer {ACCESS_TOKEN}',
    }

    response = requests.get(url, headers=headers)

    response_json = response.json()

    song_list = []
    for item in response_json.get("items", []):  
        artist_name = item.get("track", {}).get("album", {}).get("artists")[0]['name']
        song_name = item.get("track", {}).get('name') 

        if song_name: 
            song = f"{song_name} - {artist_name}"
            song_list.append(song)

    print(song_list)
    item_count = len(song_list)
    print(f"\nNumber of songs left in the playlist: {item_count}\n")
    
    return song_list


