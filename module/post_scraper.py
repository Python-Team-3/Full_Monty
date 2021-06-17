import requests 
from bs4 import BeautifulSoup
from collections import Counter

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
        comments = post.find('div', class_='comment-content')

        text = self._remove_linked_posts(body)

        return Post(title, date, text)

# gets the most used 3 words
    def _get_most_used_words(self,body) -> str:
        wordlist = []
        for each_text in body:
            # use split() to break the sentence into
            # words and convert them into lowercase
            words = body.lower().split()
 
            for each_word in words:
                wordlist.append(each_word)
            clean_wordlist(wordlist)
 
 # Function removes any unwanted symbols
    def clean_wordlist(wordlist):
 
        clean_list = []
        for word in wordlist:
            symbols = "!@#$%^&*()_-+={[}]|\;:\"<>?/., "
    
            for i in range(len(symbols)):
                word = word.replace(symbols[i], '')
    
            if len(word) > 3:
                clean_list.append(word)
        create_dictionary(clean_list)

# Creates a dictionary conatining each word's
# count and top_3 ocuuring words
    def create_dictionary(clean_list):
        word_count = {}
    
        for word in clean_list:
            if word in word_count:
                word_count[word] += 1
            else:
                word_count[word] = 1
        c = Counter(word_count)
 
        # returns the most occurring elements
        top = c.most_common(3)
        print(top)

# remove linked posts
    def _remove_linked_posts(self, body) -> str:

        selects = body.find_all("ul", {"id": "klnArticleRelatedPosts"})
        for match in selects:
            match.decompose()

        text = ""
        for tag in body:
            text += tag.text + '\n'

        return text