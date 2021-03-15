from django.views.generic import ListView
from django.shortcuts import render

from articles.models import Article


class ArticleList(ListView):
	model = Article
	template_name = 'articles/news.html'
	ordering = '-published_at'


# def articles_list(request):
# 	template = 'articles/news.html'
# 	articles = Article.objects.order_by('-published_at').prefetch_related('article_theme')
# 	context = {'articles': articles}

	# используйте этот параметр для упорядочивания результатов
	# https://docs.djangoproject.com/en/2.2/ref/models/querysets/#django.db.models.query.QuerySet.order_by

	# return render(request, template, context)
