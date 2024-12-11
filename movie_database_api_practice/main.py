import requests
import os
import pprint

imdb_token = os.environ.get('_TMDB_TOKEN_') #os.getenv('_TMDB_TOKEN_')
imdb_key = os.environ.get('_TMDB_KEY_')


def main():
    title_query = input("Movie Title: ")
    url = f"https://api.themoviedb.org/3/search/movie?query={title_query}&include_adult=false&language=en-US&page=1"
    headers = {
        'accept': 'applications/json',
        'Authorization': f'Bearer {imdb_token}'
    }
    response = requests.get(url, headers=headers)
    #print(response.text)
    data = response.json()
    query_list = data['results']
    pprint.pprint(type(query_list))

if __name__ == '__main__':
    main()
