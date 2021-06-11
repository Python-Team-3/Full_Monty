from bs4 import BeautifulSoup as soup
import bs4
import requests
import csv

class Scraper:
	URL = 'https://www.kulinarno-joana.com/'
	headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'}

	listURLS = []

	def __init__(self):
		pass		

	def getPostsURLs(self):

		pageNum = 2
		postPerPage = 12
		limitForURLS = 20

		source = requests.get(Scraper.URL, headers=Scraper.headers).text
		parser = soup(source, 'lxml')

		csvFile = open('blog_scraped_data.csv', 'w', encoding='utf-8')
		csvWriter = csv.writer(csvFile)
		csvWriter.writerow(['headline', 'timePosted', 'postURL'])

		for article in parser.find_all('article'):
			headline = article.h2.a.text

			try:
		
				timePosted = article.find('div', class_='entry-meta').time.text
				postURL = article.find('h2', class_='entry-title').a['href']
				Scraper.listURLS.append(article.find('h2', class_='entry-title').a['href']) 
		
			except Exception as e:
				timePosted = "missing"
				postURL = "broken URL"

			csvWriter.writerow([headline, timePosted, postURL])

		csvFile.close()

		return Scraper.listURLS

	def getPosts(self, list):

		postsFile = open('blog_posts.txt', 'w', encoding='utf-8')

		for urls in list:

			postSource = requests.get(urls).text
			parserPost = soup(postSource, 'lxml')

			article = parserPost.find('article')

			headline = article.h1.text

			timePosted = article.find('div', class_='entry-meta').time.text
			
			post = article.find('div', class_='entry-content')
			tagsForRemove = article.find_all('ul', id_= 'klnArticleRelatedPosts')

			for i in tagsForRemove:
				i.decompose()

			postsFile.write(headline + '\n')
			postsFile.write(timePosted + '\n\n')
			postsFile.write(post.text + '\n\n')

		postsFile.close()

scrp = Scraper()

scrp.getPostsURLs()
scrp.getPosts(scrp.listURLS)