# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import *
from django.utils.html import format_html

from django.contrib.contenttypes.admin import GenericTabularInline

from django.utils.safestring import mark_safe


# Функции фильтрации для массовой публикации/снятия с публикации.
def all_post(modeladmin, reguest, queryset):
    for qs in queryset:
        print (qs.title)

def complete_post(modeladmin, reguest, queryset):
    queryset.update(active=True)
complete_post.short_description = 'Опубликовать выбранные'

def incomplete_post(modeladmin, reguest, queryset):
    queryset.update(active=False)
incomplete_post.short_description = 'Снять с публикации'



class Book_catAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Основные настройки',        {'fields': [
            'name_block', 
            'book_cat_slug',
            'active',

            ]}),
    ]
    list_display = ['name_block', 'nomer_id', 'book_cat_slug', 'active',]
    list_display_links = ["name_block",]
    list_editable = ['active', 'nomer_id', 'book_cat_slug',]
    list_filter = [ "active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30

    #автозаполнение slug
    prepopulated_fields = {"book_cat_slug": ("name_block",)}
    actions = [all_post, complete_post, incomplete_post]


    class Meta:
        model = Book_cat

# # ////////////////////////////////////////////


class BookAdmin(admin.ModelAdmin):

    fieldsets = [
        ('Основные настройки',        {'fields': [
            'name_block',
            'book_slug', 
            'book_cat',
            'price',
            'old_price',
            'procent',
            'skidka',
            'opisanie_full',
            'opisanie_mini',
            'futured',
            'special',
            'bestseller',
            'latest',
            'active',

              ]}),
    ]
    list_display = ['name_block', 'price',
            'old_price',  'book_cat', 'futured',
            'special',
            'bestseller',
            'latest','active',]
    list_display_links = ["name_block",]
    list_editable = ['active','price',
            'old_price','futured',
            'special',
            'bestseller',
            'latest', 'book_cat',]
    list_filter = [ 'book_cat',"active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30

    actions = [all_post, complete_post, incomplete_post]

    #автозаполнение slug
    prepopulated_fields = {"book_slug": ("name_block",)}

    class Meta:
        model = Book

class ProstopagesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные настройки',        {'fields': ['name_block',  'slug', 'image',
            'text_block',  'template_name', 'active',  ]}),
        ('Сео оптимизация', {'fields': ['title_us','description',]}),
    ]
    list_display = ["name_block",  "active", 'image_img',
                    'title_us', 'description', 'slug', "created_at", ]
    list_display_links = ["name_block",]
    list_editable = ['active', 'slug',
                     'title_us', 'description', ]
    list_filter = ["active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30

  

    #автозаполнение slug
    prepopulated_fields = {"slug": ("name_block",)}




    class Meta:
        model = Prostopages



class OtzivAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные настройки',        {'fields': ['name_block', 'name_block2',
            'text_block',  'template_name', 'active',  ]}),
        
    ]
    list_display = ["name_block", "name_block2",  "active",  "created_at", ]
    list_display_links = ["name_block",]
    list_editable = ['active', ]
    list_filter = ["active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30






    class Meta:
        model = Otziv


class BlogAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные настройки',        {'fields': ['name_block', 'slug', 'image',
            'text_block',  'template_name', 'active',  ]}),
        
    ]
    list_display = ["name_block", "image_img",   "active",  "created_at", ]
    list_display_links = ["name_block",]
    list_editable = ['active', ]
    list_filter = ["active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30


    prepopulated_fields = {"slug": ("name_block",)}



    class Meta:
        model = Blog



class SliderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Основные настройки',        {'fields': ['name_block', 'image',
              'template_name', 'active',  ]}),
        
    ]
    list_display = ["name_block", "image_img",   "active",  "created_at", ]
    list_display_links = ["name_block",]
    list_editable = ['active', ]
    list_filter = ["active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30






    class Meta:
        model = Slider


admin.site.register(Book_cat, Book_catAdmin, )
admin.site.register(Book, BookAdmin, )
admin.site.register(Prostopages, ProstopagesAdmin, )
admin.site.register(Otziv, OtzivAdmin, )
admin.site.register(Blog, BlogAdmin, )
admin.site.register(Slider, SliderAdmin, )
admin.site.register(OtzivBook )