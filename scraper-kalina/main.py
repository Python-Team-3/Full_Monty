import scraper.py

if __name__ == '__main__':
    import time
    twenty_urls = UrlScraper.get_twenty_posts()
    post_scraper = PostScraper(twenty_urls)
    posts = post_scraper.get_last_posts()
    
    filename = str(time.time()) +  "posts.txt"

    for p in posts:
        p.print_to_file(filename)
