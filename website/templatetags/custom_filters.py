from django import template

register = template.Library()

@register.filter
def replace(value, args):
    """Заменяет одну строку на другую в шаблоне"""
    old, new = args.split(',')
    return value.replace(old, new)
