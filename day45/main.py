from bs4 import BeautifulSoup
import requests

response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# actual html file for the web page
web_page = response.text

soup = BeautifulSoup(web_page, "html.parser")
movie_titles = soup.find_all(class_="title")
# slice up the first 10 incorrect tags
movie_titles = movie_titles[10:]
# reverse the list
movie_titles = movie_titles[::-1]

with open("movies.txt", "w", encoding="utf-8") as file:
    for movie in movie_titles:
        file.write(f"{movie.text}\n")
