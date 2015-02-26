# -*- coding: utf-8 -*-
__author__ = 'macpro'

from django.forms import ModelForm
from models import Comments

#Подтягиваем из библиотеки Джанго форму комментария
class CommentForm(ModelForm):
	class Meta():
		model = Comments
		fields = ['comments_text']
