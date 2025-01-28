import os

from dotenv import load_dotenv

import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

from api.spotify_api import get_playlist

load_dotenv()

API_KEY = os.getenv('YT_API_KEY')
MY_PLAYLIST_ID = os.getenv('YT_PLAYLIST_ID')
SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]


def o_auth_2():

    api_service_name = "youtube"
    api_version = "v3"
    client_secrets_file = "oauth.json"

    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        client_secrets_file,
        SCOPES
    )
    credentials = flow.run_local_server(port=0)

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, credentials=credentials
    )

    return youtube


def api_auth():
    api_service_name = "youtube"
    api_version = "v3"

    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    return youtube


def get_video_ID_by_name(auth, video_name):
    request = auth.search().list(
        part="snippet",
        q=video_name,
        type="video",
    )

    response = request.execute()

    if response:
        return response['items'][0]['id']['videoId']


def add_song_to_playlist(auth, video_id, plailist_id):
    add_response = auth.playlistItems().insert(
        part="snippet",
        body={
            "snippet": {
                "playlistId": plailist_id,
                "resourceId": {
                    "kind": "youtube#video",
                    "videoId": video_id
                }
            }
        }
    ).execute()    