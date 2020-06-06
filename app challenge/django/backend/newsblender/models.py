from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=500)
	link = models.URLField()
	description = models.TextField()
	author = models.CharField(max_length=200)
	pub_date = models.DateTimeField()

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


