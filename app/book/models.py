# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

from django_ckeditor_5.fields import CKEditor5Field

#картинка в админке
from django.utils.safestring import mark_safe


# Категории книг

class Book_cat(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	active = models.BooleanField(default=True,verbose_name='Активность',)
	nomer_id = models.IntegerField(u'Номер сортировки',  null=True, blank=True)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
	book_cat_slug = models.SlugField(unique=True, max_length=255,  verbose_name='Url', db_index=True)

	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Категории книг"
		verbose_name_plural = "Категории книг"
		ordering = ["nomer_id"]

	def get_absolute_url(self):
		return "/catalog/%s/" % (self.book_cat_slug)
	
	def save(self, *args, **kwargs):
		if not self.book_cat_slug:
			lastid = Book_cat.objects.latest('id')
			self.book_cat_slug =  createslug(self.name_block)
		super(Book_cat, self).save(*args, **kwargs)




class Book (models.Model):
	name_block = models.CharField(u'Название книги', max_length=255, unique=False, null=False, blank=False)
	book_cat = models.ForeignKey('Book_cat', verbose_name='книга относится к категории', default='',  null=True, on_delete=models.CASCADE,)
	opisanie_full = CKEditor5Field(verbose_name='Описание  полное',default='', config_name='extends', null=True, blank=True)
	opisanie_mini = CKEditor5Field(verbose_name='Описание краткое',default='', config_name='extends', null=True, blank=True)
	book_slug = models.SlugField(unique=True, max_length=255,  verbose_name='Url', db_index=True)

	active = models.BooleanField(default=True,verbose_name='Активность',)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")
	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
	)

	def __str__(self):
		return self.name_block
	
	def get_absolute_url(self):
		return "/catalog/%s/%s/" % (self.kurs_cat.wiki_cat_slug,self.wiki_slug,)


	# переопределение названий
	class Meta:
		verbose_name = "Книги"
		verbose_name_plural = "Книги"
		ordering = ["-created_at"]
