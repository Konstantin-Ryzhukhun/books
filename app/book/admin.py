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
            'opisanie_full',
            'opisanie_mini',
            'active',

              ]}),
    ]
    list_display = ['name_block', 'book_slug',  'book_cat','active',]
    list_display_links = ["name_block",]
    list_editable = ['active', 'book_slug',  'book_cat',]
    list_filter = [ 'book_cat',"active","created_at",]
    search_fields = ["name_block"]
    list_per_page = 30

    actions = [all_post, complete_post, incomplete_post]

    #автозаполнение slug
    prepopulated_fields = {"book_slug": ("name_block",)}

    class Meta:
        model = Book



admin.site.register(Book_cat, Book_catAdmin, )
admin.site.register(Book, BookAdmin, )