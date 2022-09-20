#pip install beautifulsoup4
#pip install lxml

from bs4 import BeautifulSoup
with open("movies.xml", 'r') as file1:
    data = file1.read()

bs_data = BeautifulSoup(data, 'xml')

for tag in bs_data.find_all('movie',{'title':"Trigun"}):
    tag["stars"] = "what!!!!"

print(bs_data.prettify())
# write to a xml
