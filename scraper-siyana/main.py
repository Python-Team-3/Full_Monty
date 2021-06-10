#-*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import validators
import io
import urllib


class getURL():
    articleList = []
    def checkURL():
        validURL = validators.url('https://www.kulinarno-joana.com/')
        if validURL==True:
            print("URL is valid")
            url = 'https://www.kulinarno-joana.com/'
            return url;
        else:
            print("Invalid URL")
            return False;
        
    def readURL():
        url = checkURL()
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}
    
        r = requests.get(url, headers=headers)
    
        with io.open('blog.html', 'w', encoding = 'utf-8') as html_file:
            html_file.write(r.text)
            html_file.close()
        with io.open('blog.html', 'r', encoding="utf-8") as html_file:
            content = html_file.read()
        
            soup = BeautifulSoup(r.content, "html.parser")
            articles = soup.find_all("article", class_ = 'list-article')
        return articles;
def sortData():
    articles = readURL()
    for item in articles:
        title = item.find({'h2': 'entry-title'}).text
        date = item.find({'time': 'entry-date'}).text
        # link = item.find({'a': 'entry-link'})
        link = item.find('h2', class_='entry-title').a['href']
        article = {
            'title': title,
            'date': date,
            'link': link
        }
        articleList.append(article)
        # print(article)
        for key in article:
            print(key, ':', article[key])
        
def getArticle():
    # providing url
    url = "https://www.kulinarno-joana.com/2021/05/bilkova-holandska-palachinka-sas-sotirani-gubi-i-aspergi/"
    
    article_text = []
    # opening the url for reading
    html = urllib.request.urlopen(url)
      
    # parsing the html file
    htmlParse = BeautifulSoup(html, 'html.parser')
      
    text_file = open('a_file.doc', "w",  encoding = 'utf-8')
    # getting all the paragraphs
    for para in htmlParse.find_all("p"):
        article_text = para.get_text()
        text_file.write(article_text + '\n')
        print(article_text)
        
    text_file.close()
    # with open('article.txt', 'w') as txt_file:
    #     txt_file.write(str(article_text))
    #     txt_file.close()
        
getArticle()
    