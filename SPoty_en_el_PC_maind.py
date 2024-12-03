import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Configurar credenciales
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="YOUR_CLIENT_ID",
                                               client_secret="YOUR_CLIENT_SECRET",
                                               redirect_uri="YOUR_REDIRECT_URI",
                                               scope="user-read-currently-playing"))

# Obtener la canción actual
current_track = sp.current_user_playing_track()
if current_track:
    track_name = current_track['item']['name']
    artist_name = current_track['item']['artists'][0]['name']
    print(f"Reproduciendo: {track_name} - {artist_name}")
