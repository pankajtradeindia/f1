from django import template
from datetime import datetime

register = template.Library()

@register.filter(name='currency')
def currency(number):
    return "₹ "+str(number)

@register.filter()
def capfirstchar(value):
    return value.capitalize()

@register.filter()
def currentDateTime(request):
    print('datetime.now = ',datetime.now())
    return datetime.now()