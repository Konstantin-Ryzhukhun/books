#coding: utf-8

from django.urls import path, re_path
from app.book import views


urlpatterns = [
     path('catalog/<book_cat_slug>/', views.book_cat, name='book_cat'),
	path('catalog/<book_cat_slug>/<book_slug>/', views.book_full, name='book_full'),
]
