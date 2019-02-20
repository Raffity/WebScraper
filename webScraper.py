import requests
from bs4 import BeautifulSoup
import urllib.request


class WebScraper:
    def __init__(s,url):
        s.url = url
        s.pages = []
        s.result = []
        s.sauce = urllib.request.urlopen(s.url).read()
        s.soup = BeautifulSoup(s.sauce,'lxml')

    def get_pages(s):
        div = s.soup.find('div', id='otherSeasons').find_all('a')
        for link in div:
            s.pages.append(link.get('href'))

    def parse(s):
        for page in s.pages:
            div = s.soup.find('table',class_='seasons_block').find_all('td')
            for td in div:
                tr = td.find('h2')
                if(tr is not None):
                    print(tr.text)
            newURL = s.url + page
            print('\n\n'+page)
            s.sauce = urllib.request.urlopen(newURL).read()
            s.soup = BeautifulSoup(s.sauce,'lxml')

        

