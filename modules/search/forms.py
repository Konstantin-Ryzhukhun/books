# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django import forms
from app.book.models import *

class SearchTagForm(forms.Form):
    q = forms.CharField(widget=forms.TextInput(attrs={
        
        'class' : 'search-input js-search-input search-tag-query tt-input',
        'id' : 'typeahead',
        'placeholder': 'Найти книгу ...'
    }))