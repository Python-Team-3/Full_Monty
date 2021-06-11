from module.post_scraper import PostScraper

def test_scraper():
    post_scraper = PostScraper(['https://www.kulinarno-joana.com/2021/06/salata-s-proshuto-mozarela-i-iagodi/'])
    posts = post_scraper.get_last_posts()

    assert len(posts) == 1
    assert "Салата с прошуто, моцарела и ягоди" in posts[0].title