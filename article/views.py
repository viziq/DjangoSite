from django.shortcuts 			    	  import render
from django.http.response 	    		import HttpResponse, Http404
from django.template.loader 		    import get_template
from django.template 				        import Context
from django.shortcuts 				      import render_to_response, redirect
from article.models 				        import Article, Comments
from django.core.exceptions 	    	import ObjectDoesNotExist
from forms 						            	import CommentForm
from django.core.context_processors import csrf
from django.contrib				        	import auth
from django.core.paginator		    	import Paginator
from datetime					            	import datetime

#Функция вида статей
def articles(request, page_number=1):
	all_articles = Article.objects.all()
	current_page = Paginator(all_articles, 2)

	return render_to_response('articles.html', {'articles': current_page.page(page_number), 'username': auth.get_user(request).username})

#Функция комментария
def article(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)
	
#Функция добавления лайка	
def addlike(request, article_id):
	try:
		  if article_id in request.COOKIES:
			  redirect('/')
		  else:
  			article = Article.objects.get(id=article_id)
  			article.article_likes +=1
  			article.save()
  			response = redirect('/')
  			response.set_cookie(article_id, "text for like")
  			return response
	except ObjectDoesNotExist:
		raise Http404
	return redirect('/')

#Функция добавления комментария
def addcomment(request, article_id):
    if request.POST and ('pause' not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            comment.comments_from_id = auth.get_user(request).id
            comment.comments_date = datetime.now()
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True

    return redirect('/articles/get/%s/' % article_id)
