import pytest
import scraper

scrp = scraper.Scraper()

scrp.getPostsURLs()
scrp.getPosts(scrp.listURLS)

def test_connection():
	assert scrp.srouce.status_code == 200