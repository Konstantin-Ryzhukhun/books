#coding: utf-8

from django.urls import path, re_path
from app.book import views


urlpatterns = [

	path('blog/', views.blog, name='blog'),
	path('blog/<slug>/', views.blog_cat, name='blog_cat'),
	path('blog/<slug>/<post_slug>/', views.blog_full, name='blog_full'),

    path('catalog/<book_cat_slug>/', views.book_cat, name='book_cat'),
	path('catalog/<book_cat_slug>/<book_slug>/', views.book_full, name='book_full'),

	path('<slug>/', views.prostopages, name='prostopages'),
]
