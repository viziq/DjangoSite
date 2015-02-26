# -*- coding: utf-8 -*-
from django.db 					import models
from django.contrib.auth.models import User

#Создаем в базе данных поля для наших стетей
class Article(models.Model):
	class Meta():
		db_table = "article"
    	article_title = models.CharField(max_length = 200)
    	article_text = models.TextField()
    	article_date = models.DateTimeField()
    	article_likes = models.IntegerField(default=0)
	
#Создаем в базе данных поля для наших комментариев
class Comments(models.Model):
	class Meta():	
		db_table = 'comments'
    	comments_date = models.DateTimeField(auto_now_add = True)
    	comments_text = models.TextField(verbose_name="Текст комментария")
    	comments_article = models.ForeignKey(Article)
    	comments_from = models.ForeignKey(User)
