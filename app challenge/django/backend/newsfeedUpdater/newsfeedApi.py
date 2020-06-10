import feedparser

from time import mktime
from datetime import datetime

from newsblender.models import Article, Category, ArticleCategory

def update_newsfeed():
	feed = feedparser.parse("https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml")


	for article in feed.entries:
		pub_date = datetime.fromtimestamp(mktime(article.published_parsed))

		new_article = Article()
		
		new_article.title = article.title
		new_article.link = article.link
		new_article.description = article.summary
	# 	# new_article.author = article.dc:creator
		new_article.pub_date = pub_date

		new_article.save()


