This script transfers songs from a public Spotify playlist to your YouTube playlist. Here's a step-by-step explanation of what each part does:

You'll need a Spotify developer account & api key: https://developer.spotify.com/documentation/web-api

You'll also need a access to Youtube's api: https://developers.google.com/youtube/v3/getting-started

For Youtube, you need an api key and a oauth2.0 client json, which you'll name oauth.json and paste in the root of this project.

1. **Imports**: The script imports necessary modules and functions, including time for delays and various functions from

api.spotify_api

and

api.youtube_api

.

2. ## **Main Function**:

get_playlist()

: Fetches the list of songs from a specified Spotify playlist. -

api_auth()

: Authenticates with the YouTube API using an API key. -

o_auth_2()

: Authenticates with the YouTube API using OAuth 2.0 for actions that require user authorization. - For each song in the Spotify playlist: - Waits for 5 seconds (

time.sleep(5)

) to avoid hitting API rate limits. - Searches for the song on YouTube using

get_video_ID_by_name()

. - If a video ID is found, adds the song to the YouTube playlist using

add_song_to_playlist()

. - Prints a confirmation message.

3. ## **Helper Functions**:

get_playlist()

: Retrieves songs from a Spotify playlist using the Spotify API. -

api_auth()

: Authenticates with the YouTube API using an API key. -

o_auth_2()

: Authenticates with the YouTube API using OAuth 2.0. -

get_video_ID_by_name()

: Searches for a video on YouTube by name and returns the video ID. -

add_song_to_playlist()

: Adds a video to a YouTube playlist using the video ID.

### How to Run the Script

1. **Install Dependencies**:
   Ensure you have the required Python packages installed. You can use `pip` to install them:

   ```sh
   pip install requests google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
   ```

2. **Set Up API Credentials**:

   - **Spotify**: Ensure you have a valid Spotify API token.
   - **YouTube**: Ensure you have a valid API key and OAuth 2.0 credentials. Save the OAuth credentials in a file named oauth.json

3. **Environment Variables**:
   Ensure you have the following environment variables set:
   - `API_KEY`: Your YouTube API key.
   - `SCOPES`: The scopes required for YouTube API access.
   - `playlist_id`: The Spotify playlist ID.
   -

MY_PLAYLIST_ID

: The YouTube playlist ID where songs will be added.

4. **Run the Script**:
   Execute the script using Python:
   ```sh
   python main.py
   ```

This will start the process of transferring songs from the specified Spotify playlist to the specified YouTube playlist.
