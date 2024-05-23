# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#авторизация по паролю
from django.contrib.auth.models import User

#авторизация на сайте
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect

from django.db.models import Avg, Count, F, ExpressionWrapper, fields, Case, When, Value, IntegerField

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from app.book.models import *

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import forms 
from django.contrib import messages 
from app.book.forms import * 

# получение изображения по get
from PIL import Image
from io import BytesIO
from django.conf import settings
import os



from constance import config

def home(request):

	slider = Slider.objects.filter(active=True, )
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	blog = Blog.objects.filter(active=True, )[:10]


	futured = Book.objects.filter(active=True, futured=True,).annotate(
		avg_rating=Avg('otzivbook__rayting_seredina'),
		rating_percentage=ExpressionWrapper(
			F('avg_rating') / 5 * 100, output_field=fields.DecimalField()
		)
	).order_by('?').distinct()[:20]
	futured_mini = Book.objects.filter(active=True, futured=True,).annotate(
		avg_rating=Avg('otzivbook__rayting_seredina'),
		rating_percentage=ExpressionWrapper(
			F('avg_rating') / 5 * 100, output_field=fields.DecimalField()
		)
	).order_by('?').distinct()[:3]

	special = Book.objects.filter(active=True,  special=True,).annotate(
		avg_rating=Avg('otzivbook__rayting_seredina'),
		rating_percentage=ExpressionWrapper(
			F('avg_rating') / 5 * 100, output_field=fields.DecimalField()
		)
	).order_by('?').distinct()[:20]

	bestseller = Book.objects.filter(active=True, bestseller=True,).annotate(
		avg_rating=Avg('otzivbook__rayting_seredina'),
		rating_percentage=ExpressionWrapper(
			F('avg_rating') / 5 * 100, output_field=fields.DecimalField()
		)
	).order_by('?').distinct()[:20]

	latest = Book.objects.filter(active=True, latest=True,).annotate(
		avg_rating=Avg('otzivbook__rayting_seredina'),
		rating_percentage=ExpressionWrapper(
			F('avg_rating') / 5 * 100, output_field=fields.DecimalField()
		)
	).order_by('?').distinct()[:20]


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


	# response = render(request, 'index.html', {
	# 	'text':text,
	# 	'username': username,
	# 	'login_error': login_error, 
	# })

	response = render(request, 'index.html', {
		'category':category,
		'slider':slider,
		'futured':futured,
		'futured_mini':futured_mini,
		'special':special,
		'bestseller':bestseller,
		'latest':latest,
		'blog':blog,
		'otziv':otziv,
		'username': username,
		'login_error': login_error,
		'config': config 
	})

	return response



def login(request):

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


	# response = render(request, 'index.html', {
	# 	'text':text,
	# 	'username': username,
	# 	'login_error': login_error, 
	# })

	response = render(request, 'login.html', {
		'category':category,
		'futured_mini':futured_mini,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
		'config': config
	})

	return response



def register(request):

	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )

	futured_mini = Book.objects.filter(active=True, futured=True,).order_by('?')[:3]


	if request.method=='POST' and 'register' in request.POST:
		form_reg = UserForm(request.POST)
		# print(form_reg)
		# print(request.POST.get('username'))
		# print(request.POST.get('password1'))

		login = request.POST.get('username')
		passwd = request.POST.get('password1')

		if form_reg.is_valid():
			form_reg.save()
			user = auth.authenticate(username=login, password=passwd)
			auth.login(request, user)
			return HttpResponseRedirect('/')
			
	else:
		form_reg = UserForm()




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



	response = render(request, 'register.html', {
		'category':category,
		'futured_mini':futured_mini,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
		'form_reg': form_reg,
		'config': config
	})

	return response


def logout(request):
	auth.logout(request)
	return HttpResponseRedirect('/')








def handler404(request, *args, **argv):

	template = loader.get_template("404.html")
	response = HttpResponse(template.render({}, request))
	response.status_code = 404
	return response


def handler400(request, *args, **argv):

	template = loader.get_template("400.html")
	response = HttpResponse(template.render({}, request))
	response.status_code = 400
	return response


def handler403(request, *args, **argv):

	template = loader.get_template("403.html")
	response = HttpResponse(template.render({}, request))
	response.status_code = 403
	return response


def handler500(request, *args, **argv):
	
	template = loader.get_template("500.html")
	response = HttpResponse(template.render({}, request))
	response.status_code = 500
	return response