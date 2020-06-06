# from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Article

# Create your views here.

def index(request):
    article_list = Article.objects.order_by('-pub_date')
    template = loader.get_template('newsblender/index.html')
    context = {
		    'article_list': article_list
		    }
    return HttpResponse(template.render(context, request))
