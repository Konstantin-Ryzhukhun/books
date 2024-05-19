# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from datetime import datetime
from django.utils import timezone

from django_ckeditor_5.fields import CKEditor5Field

#картинка в админке
from django.utils.safestring import mark_safe


#валидация рейтинга
from django.core.validators import MaxValueValidator, MinValueValidator

from django.db.models import Avg, Max, Min, Sum

from django.contrib.auth.models import User

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
	

	price = models.DecimalField(max_digits=6, decimal_places=0, default=0, verbose_name="Цена", null=True, blank=True)
	old_price = models.DecimalField(max_digits=6, decimal_places=0, default=0, verbose_name="Цена без акции", null=True, blank=True)
	procent = models.DecimalField(max_digits=6, decimal_places=0, default=0, verbose_name="Процент скидки", null=True, blank=True)
	skidka = models.DecimalField(max_digits=6, decimal_places=0, default=0, verbose_name="Скидка в рублях", null=True, blank=True)


	futured = models.BooleanField(default=True,verbose_name='Будущее',)
	special = models.BooleanField(default=True,verbose_name='Спешл',)
	bestseller = models.BooleanField(default=True,verbose_name='Бестселлер',)
	latest = models.BooleanField(default=True,verbose_name='Последние',)

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

	def save(self, *args, **kwargs):
		# Расчет скидки и процента скидки
		if self.old_price and self.price:
			self.skidka = self.old_price - self.price
			self.procent = (self.skidka / self.old_price) * 100
		super(Book, self).save(*args, **kwargs)




class OtzivBook(models.Model):

	rayting = models.IntegerField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0),
		],
		verbose_name='Интересно',
		blank=True,
		null=True
	)
	rayting2 = models.IntegerField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0),
		],
		verbose_name='Цена',
		blank=True,
		null=True
	)
	rayting3 = models.IntegerField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0),
		],
		verbose_name='Сюжет',
		blank=True,
		null=True
	)

	rayting_seredina = models.FloatField(
		validators=[
			MaxValueValidator(5),
			MinValueValidator(0),
		],
		verbose_name='Средний рейтинг',
		blank=True,
		null=True
	)

	name_aftor = models.CharField(
		u'Имя автора',  max_length=255, unique=False, null=False, blank=False)
	
	book = models.ForeignKey(Book, on_delete=models.SET_NULL,
	                          blank=True, null=True, verbose_name='выбрать товар по id',)

	otziv_plus = CKEditor5Field(
		verbose_name='Плюсы', default='', null=True, blank=True, config_name='extends')
	
	otziv_minus = CKEditor5Field(
		verbose_name='Минусы', default='', null=True, blank=True, config_name='extends')

	opisanie = CKEditor5Field(
		verbose_name='Комментарий', default='', null=True, blank=True, config_name='extends')


	zakazchik = models.ForeignKey(User, verbose_name='Заказчик',max_length=255, null=True, blank=True, on_delete=models.SET_NULL,)


	active = models.BooleanField(default=True, verbose_name='Активность',)
	created_at = models.DateTimeField(
		auto_now_add=True, null=True, blank=True, verbose_name="Created at")
	updated_at = models.DateTimeField(
		verbose_name="Перезаписать дату отзыва", null=True, blank=True, )
	#updated_at.editable=True

	def __str__(self):
		return str(self.pk)

	# переопределение названий

	class Meta:
		verbose_name = "Отзыв на книгу"
		verbose_name_plural = "Отзывы на книги"
		ordering = ["-id"]

	def otzivrayting(self):	
		if self.rayting_seredina:
			ray = round(self.rayting_seredina / 5 * 100)
		else:
			ray = round(self.rayting / 5 * 100)
		return(ray)

	def rayting_procent(self):
		if self.rayting_seredina:
			ray = round(self.rayting_seredina / 5 * 100)
		else:
			ray = round(self.rayting / 5 * 100)
		return(ray)
	

	def save(self, *args, **kwargs):
		# Расчет скидки и процента скидки
		if self.rayting and self.rayting2 and self.rayting3:
			self.rayting_seredina = round((self.rayting + self.rayting2 + self.rayting3 ) / 3, 2)
		super(OtzivBook, self).save(*args, **kwargs)




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
		verbose_name = "Отзывы о сайте"
		verbose_name_plural = "Отзывы о сайте"
		ordering = ["created_at"]




class Blog(models.Model):
	name_block = models.CharField(u'Название', max_length=255, null=True, blank=True)
	text_block = CKEditor5Field(verbose_name='текст',default='', null=True, blank=True, config_name='extends')
	image = models.ImageField(verbose_name='Картинка',upload_to='blog',  null=True, blank=True)
	slug = models.SlugField(max_length=255, unique=True, verbose_name='Url', db_index=True)

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


	# def save(self, *args, **kwargs):
	# 	if not self.slug:
	# 		lastid = Blog.objects.latest('id')
	# 		self.slug =  createslug(self.name_block)
	# 	super(Blog, self).save(*args, **kwargs)



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
