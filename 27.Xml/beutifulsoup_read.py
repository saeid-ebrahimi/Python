#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
#read a xml file
with open("movies.xml", 'r') as file1:
    data = file1.read()
Bs_file = BeautifulSoup(data, "xml")
movies = Bs_file.find_all("movie")
print(movies)

transformers = Bs_file.find('movie', {'title': "Transformers"})
print(transformers)
stars = transformers.get("stars")
print(stars)