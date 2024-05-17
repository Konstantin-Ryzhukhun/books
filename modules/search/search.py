#==================================
# поиск
#==================================
from .forms import *
import json
from django.views.generic import *
from decimal import Decimal


def search(request):
	#поиск
	form_search = SearchTagForm()

	return  {'searchtag' : form_search,}
