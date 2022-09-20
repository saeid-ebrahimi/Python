
import csv
import requests
import xml.etree.ElementTree as ET

def loadRSS():
    # url of rss feed
    url = 'http://www.hindustantimes.com/rss/topnews/rssfeed.xml'
    resp = requests.get(url)

    with open("topnewsfeed.xml", "wb") as file1:
        file1.write(resp.content)

def parseXML(xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    news_items = []

    for item in root.findall('./channel/item'):
        # empty news dictionary
        news = {}
        for child in item:
            if child.tag == "{http:search.yahoo.com/mrss/}content":
                news['media'] = child.attrib['url']
            else:
                news[child.tag] = child.text.encode('utf8')

        # append news dictionary to news items list
        news_items.append(news)

    # return news items list
    return news_items

def savetoCSV(news_items, filename):
    # specifying the fields for csv file
    fields = ['guid','title', 'pubDate', 'description', 'link', 'media']
    # writing to csv file
    with open(filename, 'w') as csvfile:
        # creating a csv dict writer object
        writer = csv.DictWriter(csvfile, fieldnames=fields)

        # writing headers(field names)
        writer.writeheader()
        # writing data rows
        writer.writerows(news_items)

def main():
    # load rss from web to update existing xml file
    loadRSS()

    # parse xml file
    newsitems = parseXML('topnewsfeed.xml')

    # store news items in csv file
    savetoCSV(newsitems, 'topnews.csv')


if __name__ == "__main__":
    # calling main function
    main()
