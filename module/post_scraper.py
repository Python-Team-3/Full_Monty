import requests 
from bs4 import BeautifulSoup

from module.post import Post

class PostScraper():

    def __init__(self, post_urls):
        self.post_urls = post_urls

    def get_last_posts(self) -> list:
        posts = []

        for url in self.post_urls:
            posts.append(self._read_post(url))
        
        return posts
    
    def _read_post(self, url_post) -> Post:
        r = requests.get(url_post)

        soup = BeautifulSoup(r.text, features='html.parser')

        post = soup.find('article')
        title = post.find('h1', class_='entry-title').text
        date = post.find('span', class_='posted-on').time['title']
        body = post.find('div', class_='entry-content')

        text = self._remove_linked_posts(body)

        return Post(title, date, text)

    def _remove_linked_posts(self, body) -> str:

        selects = body.find_all("ul", {"id": "klnArticleRelatedPosts"})
        for match in selects:
            match.decompose()

        text = ""
        for tag in body:
            text += tag.text + '\n'

        return text