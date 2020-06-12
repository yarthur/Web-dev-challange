from django.shortcuts import redirect
from django.http import HttpResponse
from django.template import loader

from .models import Article
from newsfeedUpdater import newsfeedApi

# Create your views here.

def update(request):
	newsfeedApi.update_all_newsfeeds()
	return redirect(index)
  

def index(request):
    article_list = Article.objects.order_by('-pub_date')
    context = {
        'article_list': article_list
    }

    template = loader.get_template('newsblender/index.html')

    return HttpResponse(template.render(context, request))
