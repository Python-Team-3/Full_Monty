from os import link
from module.url_scraper import UrlScraper

def test_url_scraper():
    links = UrlScraper.get_twenty_posts()
    assert len(links) == 20
    assert links[0].startswith("https")