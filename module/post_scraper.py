import requests 
from bs4 import BeautifulSoup

from module.post import Post

class PostScraper():

    def __init__(self, post_urls):
        self.post_urls = post_urls


    # gets the posts from blog and append them to list
    def get_last_posts(self) -> list:
        posts = []

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
        paragraphs = self._get_paragraphs(body)

        comments_soup = soup.find('ol', class_='comment-list')

        comments = None if comments_soup is None else self._get_comments(comments_soup) 

        text = self._remove_linked_posts(body)

        return Post(title, date, text, comments=comments, first_paragraphs=paragraphs)

    def _get_paragraphs(self, body):
        paragraphs = []

        for paragraph in body.find_all('p'):
            self._remove_images(paragraph)
            paragraph_text = paragraph.text
            if len(paragraph_text) > 0:
                paragraphs.append(paragraph_text)

        return paragraphs

    def _remove_images(self, paragraph):
        for photo in paragraph.findChildren('img'):
            photo.decompose()

    def _get_comments(self, comments_soup):

        comments_list = []
        for li in comments_soup.find_all('li'):
            comment_text = li.find('div', class_='comment-content').text
            comment_author = self._remove_children(li.find('footer', class_='comment-meta'))
            comments_list.append((comment_author, comment_text))

        return comments_list

    def _remove_children(self, comment_author) -> str:
        for child in comment_author.findChildren():
            child.decompose()
        return comment_author.text.strip()

    # remove linked posts
    def _remove_linked_posts(self, body) -> str:

        selects = body.find_all("ul", {"id": "klnArticleRelatedPosts"})
        for match in selects:
            match.decompose()

        text = ""
        for tag in body:
            text += tag.text + '\n'

        return text