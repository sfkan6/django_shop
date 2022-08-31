from django import template

register = template.Library()

@register.filter
def rating_star(num):
    return int(num) * '\u2605'

