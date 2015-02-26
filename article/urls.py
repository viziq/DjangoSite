from django.conf.urls import patterns, include, url

urlpatterns = patterns('',

#Работа всех урл страниц:
    url(r'^articles/all/$', 'article.views.articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'article.views.article'),
	  url(r'^articles/addlike/(?P<article_id>\d+)/$', 'article.views.addlike'),
	  url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'article.views.addcomment'),
    url(r'^page/(\d+)/$', 'article.views.articles'),
    url(r'^', 'article.views.articles'),
)	
