from django.db import models

# Create your models here.

class Article(models.Model):
	title = models.CharField(max_length=500)
	link = models.URLField()
	description = models.TextField()
	author = models.CharField(max_length=200, null=True, blank=True)
	pub_date = models.DateTimeField()

	def save(self, *args, **kwargs):
		if Article.objects.filter(link=self.link).exists():
			return Article.objects.filter(link=self.link)


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


