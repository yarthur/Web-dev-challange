import feedparser

from time import mktime
from datetime import datetime

from newsblender.models import Article, Category, ArticleCategory, Feed

def update_all_newsfeeds():
	feeds = Feed.objects.all()

	for feed in feeds:
		update_newsfeed(feed)

def update_newsfeed(feed):
	feedData = feedparser.parse(feed.url, etag=feed.etag, modified=feed.modified)

	if feedData.status == 200:
		feed.imageSrc = feedData.feed.image.href if hasattr(feedData.feed, "image") else None

		# For improved feed processing -- no need to pull down if there are no new updates
		feed.etag = feedData.etag if hasattr(feedData, "etag") else None
		feed.modified = feedData.modified if hasattr(feedData, "modified") else None

		feed.save()

		for article in feedData.entries:

			try:
				pub_date = datetime.fromtimestamp(mktime(article.published_parsed))

				new_article = Article()

				new_article.title = article.title
				new_article.link = article.link
				new_article.description = article.summary
				new_article.author = article.author if hasattr(article, "author") else None
				new_article.pub_date = pub_date
				new_article.feed = feed

				if hasattr(article, 'media_content') and article.media_content[0]["medium"] == 'image':
					new_article.imageSrc = article.media_content[0]['url']

				new_article.save()
			except:
				pass
