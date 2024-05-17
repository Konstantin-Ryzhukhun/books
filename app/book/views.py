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




def book_cat(request, book_cat_slug):


	book_cat_all = book_cat.objects.all().order_by('nomer_id')

	book_cat = get_object_or_404(book_cat, book_cat_slug=book_cat_slug)
	book = Book.objects.filter(active=True, kurs_cat=book_cat)


	paginator = Paginator(book, 30)
	page = request.GET.get('page')
	try:
		book = paginator.page(page)
	except PageNotAnInteger:
		book = paginator.page(1)
	except EmptyPage:
		book = paginator.page(paginator.num_pages)

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
		'book_cat_all':book_cat_all,
		'book_cat':book_cat,
		'tasks':tasks,
		'username': username,
		'login_error': login_error, 
	})


	if not request.user.is_authenticated:
		return HttpResponseRedirect('/')
	else:
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