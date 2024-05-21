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

from constance import config

def blog(request):
	
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

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	response = render(request, 'book/blog.html', {
		'category':category,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
		'config': config
	})
	return response

def blog_cat(request, slug):
	
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

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	response = render(request, 'book/blog_cat.html', {
		'category':category,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
		'config': config
	})
	return response

def blog_full(request, slug,  post_slug):

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

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )

	response = render(request, 'book/blog_full.html', {
		'category':category,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
		'config': config
	})
	return response


def prostopages(request, slug):

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

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )

	prostopages = get_object_or_404(Prostopages.objects.filter(active=True),slug=slug,)

	response = render(request, 'book/prostopages.html', {
		'prostopages':prostopages,
		'category':category,
		'otziv':otziv, 
		'username': username,
		'login_error': login_error, 
		'config': config
	})
	return response



def book_cat(request, book_cat_slug):


	# book_cat_all = Book.objects.all()

	# book_cat = get_object_or_404(Book, book_cat_slug=book_cat_slug)
	# book = Book.objects.filter(active=True, kurs_cat=book_cat)

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	futured_mini = Book.objects.filter(active=True, futured=True,).order_by('?')[:3]


	book_cat = get_object_or_404(Book_cat.objects.filter(active=True, book_cat_slug=book_cat_slug) )

	tovar_all = Book.objects.filter(active=True, book_cat=book_cat).order_by('-created_at')

	paginator = Paginator(tovar_all, 12)
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
		'futured_mini':futured_mini,
		# 'book_cat_all':book_cat_all,
		# 'book_cat':book_cat,
		# 'tasks':tasks,
		'username': username,
		'login_error': login_error, 
		'config': config
	})

	return response
	

def book_full(request, book_cat_slug, book_slug):



	book = get_object_or_404(Book, book_slug=book_slug)

	book_dop = Book.objects.filter(active=True, book_cat=book.book_cat).order_by('?')[:20]
	otziv_book = OtzivBook.objects.filter(active=True, book=book)

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	futured_mini = Book.objects.filter(active=True, futured=True,).order_by('?')[:3]

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
		'otziv':otziv, 
		'book_dop':book_dop,
		'otziv_book':otziv_book,
		'futured_mini':futured_mini,
		'category':category,
		'book':book,
		'username': username,
		'login_error': login_error, 
		'config': config
	})



	return response