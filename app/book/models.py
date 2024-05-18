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
	image = models.ImageField(verbose_name='Картинка',upload_to='prostopages',  null=True, blank=True)
	image2 = models.ImageField(verbose_name='Картинка',upload_to='prostopages',  null=True, blank=True)

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



class Prostopages(models.Model):
	name_block = models.CharField(u'Заголовок h1', max_length=255, null=True, blank=True)
	text_block = CKEditor5Field(verbose_name='Описание страницы',default='', null=True, blank=True, config_name='extends')
	image = models.ImageField(verbose_name='Картинка',upload_to='prostopages',  null=True, blank=True)

	active = models.BooleanField(default=True,verbose_name='Активность',)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

	slug = models.SlugField(max_length=255, unique=True, verbose_name='Url', db_index=True)
	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'book/prostopages.html'. Если не указано,  "
			"система будет использовать 'prostopages/prostopages.html'."
		),
	)
	title_us = models.CharField(u'Тайтл', max_length=255, null=True, blank=True)
	description = models.TextField(u'Дескрипшон', null=True, blank=True )
	

	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Простую страницу"
		verbose_name_plural = "Простые страницы"
		ordering = ["created_at"]

	def get_absolute_url(self):
		return "/%s/" % (self.slug)

	# картинка в админке
	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'


	def save(self, *args, **kwargs):
		if not self.slug:
			lastid = Prostopages.objects.latest('id')
			self.slug =  createslug(self.name_block)
		super(Prostopages, self).save(*args, **kwargs)



class Otziv(models.Model):
	name_block = models.CharField(u'Имя', max_length=255, null=True, blank=True)
	name_block2 = models.CharField(u'Должность', max_length=255, null=True, blank=True)
	text_block = CKEditor5Field(verbose_name='комментарий',default='', null=True, blank=True, config_name='extends')

	active = models.BooleanField(default=True,verbose_name='Активность',)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'book/prostopages.html'. Если не указано,  "
			"система будет использовать 'prostopages/prostopages.html'."
		),
	)


	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Отзывы"
		verbose_name_plural = "Отзывы"
		ordering = ["created_at"]




class Blog(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	text_block = CKEditor5Field(verbose_name='текст',default='', null=True, blank=True, config_name='extends')
	image = models.ImageField(verbose_name='Картинка',upload_to='blog',  null=True, blank=True)

	active = models.BooleanField(default=True,verbose_name='Активность',)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'book/prostopages.html'. Если не указано,  "
			"система будет использовать 'prostopages/prostopages.html'."
		),
	)


	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Новость"
		verbose_name_plural = "Новость"
		ordering = ["created_at"]

	def get_absolute_url(self):
		return "/%s/" % (self.slug)



	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'


	def save(self, *args, **kwargs):
		if not self.slug:
			lastid = Blog.objects.latest('id')
			self.slug =  createslug(self.name_block)
		super(Blog, self).save(*args, **kwargs)



class Slider(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	image = models.ImageField(verbose_name='Картинка',upload_to='blog',  null=True, blank=True)

	active = models.BooleanField(default=True,verbose_name='Активность',)
	created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated at")

	template_name = models.CharField(
		('Выбор шаблона'),
		max_length=70,
		blank=True,
		help_text=(
			"Пример: 'book/prostopages.html'. Если не указано,  "
			"система будет использовать 'prostopages/prostopages.html'."
		),
	)


	def __str__(self):
		return self.name_block

	# переопределение названий
	class Meta:
		verbose_name = "Слайдер"
		verbose_name_plural = "Слайдер"
		ordering = ["created_at"]




	def image_img(self,):
		if self.image:
			return mark_safe('<a href="{0}" target="_blank"><img src="{0}" width="100" /></a>' .format(self.image.url))
		else:
			return '(Нет изображения)'
	image_img.short_description = 'Картинка'
