from django import template
from django.db.models import Avg, Max, Min, Sum

register = template.Library()

@register.filter()
def raytingstars(value,):
    print(value)
    rayting_sr = value.aggregate(Avg('rayting'))
    print(rayting_sr)
    if rayting_sr['rayting__avg'] is not None:
        rayting_sr_int = rayting_sr['rayting__avg']
        # print(rayting_sr_int)
        rayting_sr_procent = round(rayting_sr_int / 5 * 100) 
    else:
        rayting_sr_procent = ''
    return [rayting_sr_procent,rayting_sr_int]

