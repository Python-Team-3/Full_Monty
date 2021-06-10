import requests
from bs4 import BeautifulSoup

class Scraper:
    def __init__(self):
        url = 'https://www.kulinarno-joana.com/'
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
        self.r=requests.get(url,headers=headers)
        self.soup = BeautifulSoup(self.r.content, features='lxml')
    
    def scrapeSite(self):
        self.scraped = self.soup.find_all('article')
    
    def makeList(self):
        self.scrapedList=[]
        for item in self.scraped:
            title = item.find('h2',class_='entry-title').text
            self.scrapedList.append(title)
            print(title)

s = Scraper()
s.scrapeSite()
s.makeList()