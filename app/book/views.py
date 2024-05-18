# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from .models import *

#авторизация по паролю
from django.contrib.auth.models import User

#авторизация на сайте
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.shortcuts import redirect
from django.shortcuts import get_object_or_404

def blog(request):
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	response = render(request, 'book/blog.html', {
		'category':category,
		'otziv':otziv,
	})
	return response

def blog_cat(request, slug):
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	response = render(request, 'book/blog_cat.html', {
		'category':category,
		'otziv':otziv,
	})
	return response

def blog_full(request, slug,  post_slug):
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )

	response = render(request, 'book/blog_full.html', {
		'category':category,
		'otziv':otziv,
	})
	return response


def prostopages(request, slug):
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )

	prostopages = get_object_or_404(Prostopages.objects.filter(active=True),slug=slug,)

	response = render(request, 'book/prostopages.html', {
		'prostopages':prostopages,
		'category':category,
		'otziv':otziv, 
	})
	return response



def book_cat(request, book_cat_slug):


	# book_cat_all = Book.objects.all()

	# book_cat = get_object_or_404(Book, book_cat_slug=book_cat_slug)
	# book = Book.objects.filter(active=True, kurs_cat=book_cat)

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )


	book_cat = get_object_or_404(Book_cat.objects.filter(active=True, book_cat_slug=book_cat_slug) )

	tovar_all = Book.objects.filter(active=True, book_cat=book_cat).order_by('-created_at').distinct()


	paginator = Paginator(tovar_all, 30)
	page = request.GET.get('page')
	try:
		tovar_all = paginator.page(page)
	except PageNotAnInteger:
		tovar_all = paginator.page(1)
	except EmptyPage:
		tovar_all = paginator.page(paginator.num_pages)

	# авторизация под админом
	username = auth.get_user(request).username
	login_error = ''
	if request.method=='POST' and 'autorization' in request.POST:
		username = request.POST.get('username',)
		password = request.POST.get('password',)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			login_error = 'Пользователь не найден'

	response = render(request, 'book/book_cat.html', {
		'book_cat':book_cat,
		'tovar_all':tovar_all,
		'category':category,
		'otziv':otziv, 
		# 'book_cat_all':book_cat_all,
		# 'book_cat':book_cat,
		# 'tasks':tasks,
		# 'username': username,
		# 'login_error': login_error, 
	})

	return response
	

def book_full(request, book_cat_slug, book_slug):

	book_cat_all = book_cat.objects.all().order_by('nomer_id')

	book_full = get_object_or_404(Book, book_slug=book_slug)

	book = Book.objects.filter(active=True, kurs_cat__id=book_full.kurs_cat.id).order_by('?').distinct()[:8]

	# авторизация под админом
	username = auth.get_user(request).username
	login_error = ''
	if request.method=='POST' and 'autorization' in request.POST:
		username = request.POST.get('username',)
		password = request.POST.get('password',)
		user = auth.authenticate(username=username, password=password)
		if user is not None:
			auth.login(request, user)
			return HttpResponseRedirect('/')
		else:
			login_error = 'Пользователь не найден'

	response = render(request, 'book/book_full.html', {
		'book_cat_all':book_cat_all,
		'book_full':book_full,
		'book':book,
		'username': username,
		'login_error': login_error, 
	})


	if not request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
		return response