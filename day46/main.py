import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# constants
SPOTIFY_CLIENT_ID_ = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET_ = os.environ.get("_SPOTIFY_CLIENT_SECRET_")
SPOTIPY_URI = "http://example.com"
SPOTIFY_USER_ID = "1236246968"
SCOPE = "playlist-modify-private"

# spotify authentication using spotipy
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=SCOPE,
    client_id=SPOTIFY_CLIENT_ID_,
    client_secret=SPOTIFY_CLIENT_SECRET_,
    redirect_uri=SPOTIPY_URI))

def get_billboard_top_100(date):
    """
    takes a date in time, uses BeautifulSoup to retrieve Billboard's top 100 songs on that date.
    :param date: String in the format of 'YYYY-MM-DD'
    :return:list of top 100 songs' names
    """
    # create connection to site, grab it's raw text, 'make it into soup'
    response = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
    web_page_text = response.text
    soup = BeautifulSoup(web_page_text, "html.parser")
    # define the class string that coincides with the titles of the top 100 songs
    class_name = ("c-title a-no-trucate a-font-primary-bold-s u-letter-spacing-0021 lrv-u-font-size-18@tablet "
                  "lrv-u-font-size-16 u-line-height-125 u-line-height-normal@mobile-max a-truncate-ellipsis "
                  "u-max-width-330 u-max-width-230@tablet-only")
    title_list = soup.find_all(name="h3", id="title-of-a-story", class_=class_name)
    top_100_titles_list = []
    for song in title_list:
        track_name = song.text.strip()
        year = date.split("-")[0]
        pair = {track_name: year}
        top_100_titles_list.append(pair)
    return top_100_titles_list


def create_track_uri_list(top_100_list):
    track_uri_list = []
    for song in top_100_list:
        for track_name, year in song.items():
            result = sp.search(q=f"year%3A{year}track%3A{track_name}", limit=1)
            try:
                track_uri = result["tracks"]['items'][0]['uri']
                track_uri_list.append(track_uri)
            except IndexError:
                print(f"{song} not found in Spotify. Skipped")
    return track_uri_list


def create_playlist(spot_usr_id, date, playlist_description, track_uri_list):
    playlist_response = sp.user_playlist_create(user=spot_usr_id,
                                                name=f"{date} Billboard 100",
                                                public=False,
                                                description=playlist_description)
    sp.playlist_add_items(playlist_id=playlist_response["id"], items=track_uri_list)


def main():
    date = input("What year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
    top_100_songs = get_billboard_top_100(date)
    track_uri_list = create_track_uri_list(top_100_list=top_100_songs)
    create_playlist(SPOTIFY_USER_ID, date, f"Top 100 on {date}", track_uri_list)
    print(f"Playlist for {date} Billboard 100 created successfully!")


if __name__ == "__main__":
    main()