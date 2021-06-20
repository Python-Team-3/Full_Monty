from module.url_scraper import UrlScraper
from module.post_scraper import PostScraper
from module.post import Post
import time

if __name__ == '__main__':
    
    twenty_urls = UrlScraper.get_twenty_posts()
    post_scraper = PostScraper(twenty_urls)
    filename = str(time.time()) +  "posts"

    scraped_posts = []

    for p in post_scraper.get_last_posts():
        scraped_posts.append(p.get_as_json_object())
    
    Post.print_to_json_file(scraped_posts, filename)
