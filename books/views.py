# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#авторизация по паролю
from django.contrib.auth.models import User

#авторизация на сайте
from django.contrib import auth
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
import json

from app.book.models import *

# получение изображения по get
from PIL import Image
from io import BytesIO
from django.conf import settings
import os


def home(request):

	slider = Slider.objects.filter(active=True, )
	otziv = Otziv.objects.filter(active=True, )
	category = Book_cat.objects.filter(active=True, )
	blog = Blog.objects.filter(active=True, )[:10]

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
		'blog':blog,
		'otziv':otziv,
		'username': username,
		'login_error': login_error, 
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