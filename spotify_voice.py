import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import sys
import subprocess

client_id = "your_client_id"
client_secret = "your_client_secret"
redirect_uri = "http://127.0.0.1:8000/callback"

query = " ".join(sys.argv[1:])
scope = "user-read-playback-state user-modify-playback-state user-library-read playlist-modify-public"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=client_id,
    client_secret=client_secret,
    redirect_uri=redirect_uri,
    scope=scope
))

results = sp.search(q=query, type='track,album,artist,playlist', limit=5)

# Try to find the best match - prioritize tracks, then albums, then artists, then playlists
found_item = None

if results['tracks']['items']:
    found_item = results['tracks']['items'][0]
elif results['albums']['items']:
    found_item = results['albums']['items'][0]
elif results['artists']['items']:
    found_item = results['artists']['items'][0]
elif results['playlists']['items']:
    found_item = results['playlists']['items'][0]

if found_item:
    spotify_url = found_item['external_urls']['spotify']
    
    # Try to open in Spotify desktop app first
    try:
        # Convert web URL to Spotify URI for desktop app
        spotify_uri = found_item['uri']
        subprocess.run(['open', '-a', 'Spotify', spotify_uri], check=True)
        print(f"Opening in Spotify app: {found_item['name']}")
    except (subprocess.CalledProcessError, KeyError):
        # Fallback to web player if desktop app fails
        webbrowser.open(spotify_url)
        print(f"Opening in web player: {found_item['name']}")
else:
    print("No results found on Spotify.")
