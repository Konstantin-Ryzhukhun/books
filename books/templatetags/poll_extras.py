from django import template

register = template.Library()

@register.filter()
def distinct(items):
	return set(items)