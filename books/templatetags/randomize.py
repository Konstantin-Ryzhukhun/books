from django import template
import random

register = template.Library()

@register.filter
def randomize(value):
    temp_list = list(value)
    random.shuffle(temp_list)
    return temp_list