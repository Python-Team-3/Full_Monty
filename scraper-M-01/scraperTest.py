import pytest
import scraper

s = scraper.Scraper()
s.scrapeSite()
s.makeList()

def test_method01():
    assert s.r.status_code == 200

def test_method02():
    assert type(s.scrapedList) == type(['jaja','gaga'])

def test_method03():
    assert type(s.scrapedList[0]) == type('jaja')

def test_method04():
    assert 'Салата от краставици с резене и халуми' in s.scrapedList[0]

def test_method05():
    assert 'Салата с прошуто, моцарела и ягоди' in s.scrapedList[1] 

def test_method06():
    assert 'Билкова холандска палачинка със сотирани гъби и аспержи' in s.scrapedList[2]

def test_method07():
    assert 'Обърнат сладкиш с шамфъстък и ревен' in s.scrapedList[3]

def test_method08():
    assert 'Салата от аспержи с билки и рохки яйца' in s.scrapedList[4]


