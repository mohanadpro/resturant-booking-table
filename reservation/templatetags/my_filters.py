from django import template

register = template.Library()

@register.filter(name="times")
def times(number):
    return range(1,number)

@register.filter(name="specific_time")
def specific_time(number):
    x = number+10
    if x == 24:
        x = "00"
    return str(x)+":00"