# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from app.book.models import *

#==================================
# поиск
#==================================
from django.db.models import Q
from modules.search.forms import *
import json
from django.views.generic import *
from decimal import Decimal
from django.http import Http404, HttpResponse, HttpResponsePermanentRedirect
from fuzzywuzzy import fuzz
import pymorphy2


# вывод json формата поля Declimed с округлением до целого
class DecimalEncoder(json.JSONEncoder):
	def default(self, obj):
		if isinstance(obj, Decimal):
			#print (obj)
			a = float(obj)
			b = round(a)
			return b
		return json.JSONEncoder.default(self, obj)

class TagJson(View):
# 	""" Search tags with autocomplete (live search) json data"""
	def get(self, request):
		q = request.GET.get('q', '')
		taglist = []

		tasks = Tasks.objects.filter(
			Q(name_block__icontains=q) |
			Q(opisanie_full__icontains=q)
		).distinct()

		# print(tovars)

		if not tasks:  # Если результаты фильтрации пусты
			similarity_list = []

			for task in Tasks.objects.all():
				if task.name_block is not None:
					similarity = fuzz.ratio(task.name_block.lower(), q.lower())  # Производим сравнение

					if similarity > 60:

						task_full_url = task.kurs_cat.wiki_cat_slug+"/"+task.wiki_slug

						new = {
							'q' : task.name_block, 
							'url' : task_full_url,
							'type': 'tovar',
						}
						taglist.append(new)

			return HttpResponse(json.dumps(taglist), content_type="application/json")
        

		
		for task in tasks:

			task_full_url = task.kurs_cat.wiki_cat_slug+"/"+task.wiki_slug

			new = {
				'q' : task.name_block, 
				'url' : task_full_url,

				'type': 'tovar',
			
			}
			taglist.append(new)


		return HttpResponse(json.dumps(taglist),content_type="application/json")




# class FamilyJson(View):
# # 	""" Search tags with autocomplete (live search) json data"""
# 	def get(self, request):
# 		q = request.GET.get('q', '')
# 		taglist = []

# 		family = Family_tree.objects.filter(
# 			Q(name__icontains=q) |
# 			Q(otchestvo__icontains=q) |
# 			Q(familiya__icontains=q) |
# 			Q(date1__icontains=q) |
# 			Q(date2__icontains=q)
# 		).distinct()

# 		# print(tovars)

# 		if not family:  # Если результаты фильтрации пусты
# 			similarity_list = []

# 			for family in Family_tree.objects.all():
# 				if family.name is not None:
# 					similarity = fuzz.ratio(family.name.lower(), q.lower())  # Производим сравнение

# 					if similarity > 60:

# 						# family_full_url = task.kurs_cat.wiki_cat_slug+"/"+task.wiki_slug

# 						new = {
# 							'q' : family.name, 
# 							# 'url' : task_full_url,
# 							'type': 'tovar',
# 						}
# 						taglist.append(new)

# 			return HttpResponse(json.dumps(taglist), content_type="application/json")
        

		
# 		for family in familys:

# 			# task_full_url = task.kurs_cat.wiki_cat_slug+"/"+task.wiki_slug

# 			new = {
# 				'q' : task.name_block, 
# 				# 'url' : task_full_url,

# 				'type': 'tovar',
			
# 			}
# 			taglist.append(new)


# 		return HttpResponse(json.dumps(taglist),content_type="application/json")