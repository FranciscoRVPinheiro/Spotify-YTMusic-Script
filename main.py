import os
import time

from api.spotify_api import get_playlist
from api.youtube_api import o_auth_2, api_auth, get_video_ID_by_name, add_song_to_playlist, MY_PLAYLIST_ID


def main():
    songs_list = get_playlist()
    youtube_api_key = api_auth()
    youtube_oauth = o_auth_2()
    for song in songs_list:
        time.sleep(5)
        video_id = get_video_ID_by_name(youtube_api_key, song)
        if video_id:
            add_song_to_playlist(youtube_oauth, video_id, MY_PLAYLIST_ID)
            print(f'{song} - Done.')
        else:
            continue


if __name__ == "__main__":
    main()