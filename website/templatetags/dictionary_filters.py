from django import template

register = template.Library()

@register.filter
def get_dict_value(dictionary, key):
    """Получает значение из словаря по ключу"""
    if isinstance(dictionary, dict):
        return dictionary.get(key, "")
    return ""
