import feedparser

from time import mktime
from datetime import datetime

from newsblender.models import Article, Category, ArticleCategory

def update_all_newsfeeds():
	feeds = [
			"https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml",
			"https://www.polygon.com/rss/index.xml"
			"http://feeds.foxnews.com/foxnews/latest",
		]

	for url in feeds:
		update_newsfeed(url)

def update_newsfeed(feedUrl):
	feed = feedparser.parse(feedUrl)


	for article in feed.entries:
		try:
			pub_date = datetime.fromtimestamp(mktime(article.published_parsed))

			new_article = Article()
			
			new_article.title = article.title
			new_article.link = article.link
			new_article.description = article.summary
		# 	# new_article.author = article.dc:creator
			new_article.pub_date = pub_date

			new_article.save()
		except:
			return None

