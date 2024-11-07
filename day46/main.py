import requests
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
load_dotenv()

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/",
        client_id=os.environ["client_id"],
        client_secret=os.environ["client_secret"],
        show_dialog=True,
        cache_path="day46/token.txt",
        username="cmanh75", 
    )
)
user_id = sp.current_user()["id"]

date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")

header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) Gecko/20100101 Firefox/131.0"}
response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{date}", headers=header)
website_html = BeautifulSoup(response.text, "html.parser")
song_names_spans = website_html.select("li ul li h3")
songs = [song.getText().strip() for song in song_names_spans]


year = date.split("-")[0]
song_uris = []
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except:
        print(f"{song} doesn't exist in Spotify")
playlist = sp.user_playlist_create(
    user=os.environ["user_id"],
    name=f"{date} Billboard 100",
    public=False
)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
