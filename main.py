from module.url_scraper import UrlScraper
from module.post_scraper import PostScraper
import module.post
import json

if __name__ == '__main__':

    twenty_urls = UrlScraper.get_twenty_posts()
    post_scraper = PostScraper(twenty_urls)
    filename = str(time.time()) +  "posts.json"
    posts = post_scraper.get_last_posts()
    for p in posts:
        p.print_to_file(filename)