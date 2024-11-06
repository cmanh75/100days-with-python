import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
movie_title = [title.getText() for title in all_titles]
movie_title.reverse()

with open("day45/movie.txt", "w", encoding="utf-8") as file:
    for movie in movie_title:
        file.write(f"{movie}\n")