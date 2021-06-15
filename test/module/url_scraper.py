import requests 
from bs4 import BeautifulSoup

class UrlScraper():

    # gets the blog`s url
    BLOG_URL = 'https://www.kulinarno-joana.com/'
    POSTS_TO_SCRAPE = 20

    def __init__(self):
        pass

# save the posts` data to a list 
    def _get_post_urls(page_url) -> list:
        r = requests.get(UrlScraper.BLOG_URL)
        soup = BeautifulSoup(r.text, features='html.parser')
        articles = soup.find_all("article")
        url_list = []
        for article in articles:
            url_list.append(article.find('h2', class_='entry-title').a['href'])

        return url_list

# save the data for 20 posts
    def get_twenty_posts() -> list:
        urls = []
        page_number = 1
        while len(urls) < UrlScraper.POSTS_TO_SCRAPE: 
            page_url = UrlScraper.BLOG_URL + f"page/{page_number}/"
            urls.extend(UrlScraper._get_post_urls(page_url))
            page_number += 1
        return urls[0:UrlScraper.POSTS_TO_SCRAPE]