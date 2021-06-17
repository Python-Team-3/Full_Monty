import requests 
from bs4 import BeautifulSoup
from collections import Counter
import re

from module.post import Post

class PostScraper():

    def __init__(self, post_urls):
        self.post_urls = post_urls

# gets the posts from blog and append them to list
    def get_last_posts(self) -> list:
        posts = []
        i = 0
        for url in self.post_urls:
            posts.append(self._read_post(url))
        
        return posts
    
# read posts from blog
    def _read_post(self, url_post) -> Post:
        r = requests.get(url_post)

        soup = BeautifulSoup(r.text, features='html.parser')

        post = soup.find('article')
        title = post.find('h1', class_='entry-title').text
        date = post.find('span', class_='posted-on').time['title']
        body = post.find('div', class_='entry-content')
      
        commentsSection = soup.find(id = 'comments')
        comments = self._get_comments(commentsSection)

        text = self._remove_linked_posts(body)
        common = self._get_most_common_words(text.split())

        return Post(title, date, text, comments, common)

    def _get_most_common_words(self, word_list):

        words_to_count = (word for word in word_list if len(word)>3)
        c = Counter(words_to_count)
        return c.most_common(3)


# remove linked posts
    def _remove_linked_posts(self, body) -> str:

        selects = body.find_all("ul", {"id": "klnArticleRelatedPosts"})
        for match in selects:
            match.decompose()

        text = ""
        for tag in body:
            text += tag.text + '\n'

        return text

    def _get_comments(self, body) -> str: 
        selects = body.find_all("li", id = re.compile('^comment-'))

        data = {}
        data['comments'] = []
        
        for tag in selects:
            data['comments'].append({
            tag.find("footer", class_='comment-meta').text : tag.find("div", class_='comment-content').text
            
            })
        return data