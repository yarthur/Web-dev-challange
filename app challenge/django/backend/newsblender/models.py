from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=500)
	link = models.URLField()
	description = models.TextField()
	author = models.CharField(max_length=200, null=True, blank=True)
	pub_date = models.DateTimeField()
	feed = models.ForeignKey('Feed', on_delete = models.CASCADE, null=True, editable=False)
	imageSrc = models.URLField(null=True, blank=True, editable=False)

	def save(self, *args, **kwargs):
		if Article.objects.filter(link=self.link).exists():
			old_self = Article.objects.filter(link=self.link)[0]
			self.pk = old_self.pk


		return super(Article, self).save(*args, **kwargs)


class Category(models.Model):
	name = models.CharField(max_length=200)

class ArticleCategory(models.Model):
	article = models.ForeignKey(
		'Article',
		on_delete = models.CASCADE,
	)
	category = models.ForeignKey(
		'Category',
		on_delete = models.CASCADE,
	)

class Feed(models.Model):
	name = models.CharField(max_length=200)
	url = models.URLField()
	imageSrc = models.URLField(null=True, editable=False)
	etag = models.CharField(max_length=200, null=True, blank=True, editable=False)
	modified = models.CharField(max_length=200, null=True, blank=True, editable=False)

	def __str__(self):
		return self.name
