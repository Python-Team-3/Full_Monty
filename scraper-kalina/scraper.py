import requests 
from bs4 import BeautifulSoup


class UrlScraper():

    BLOG_URL = 'https://www.kulinarno-joana.com/'

    def __init__(self):
        pass

    def _get_post_urls(page_url):
        r = requests.get(UrlScraper.BLOG_URL)
        soup = BeautifulSoup(r.text, features='html.parser')
        articles = soup.find_all("article")
        url_list = []
        for article in articles:
            url_list.append(article.find('h2', class_='entry-title').a['href'])

        return url_list

    def get_twenty_posts():
        urls = []
        page_number = 1
        while len(urls) < 20: 
            page_url = UrlScraper.BLOG_URL + f"page/{page_number}/"
            urls.extend(UrlScraper._get_post_urls(page_url))
            page_number += 1
        return urls[0:20]


class Post():
    
    def __init__(self, title, date, text) -> None:
        self.title = title
        self.date = date
        self.text = text
    
    def print_to_file(self, filename):
        with open(filename, 'a+') as f:
            f.write(self.title + '\n')
            f.write(self.date + '\n')
            f.write(self.text + '\n')
            f.write((20 * '-') + '\n')


class PostScraper():

    def __init__(self, post_urls):
        self.post_urls = post_urls

    def get_last_posts(self):
        posts = []

        for url in self.post_urls:
            posts.append(self._readPost(url))
        
        return posts
    
    def _readPost(self, url_post):
        r = requests.get(url_post)

        soup = BeautifulSoup(r.text, features='html.parser')

        post = soup.find('article')
        title = post.find('h1', class_='entry-title').text
        date = post.find('span', class_='posted-on').time['title']
        text = post.find('div', class_='entry-content').text

        return Post(title, date, text)
