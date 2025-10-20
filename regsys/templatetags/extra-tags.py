from django import template
register = template.Library()

@register.filter
def index(indexable, i):
    return indexable[i]
    
@register.filter
def subtract(value, arg):
    return value - arg

@register.filter
def get_item(dictionary, key):
    """Достаёт значение из словаря по ключу"""
    if dictionary is None:
        return []
    return dictionary.get(key, [])

@register.filter
def subtract(value, arg):
    """Вычитание: value - arg"""
    return value - arg

@register.filter
def join_if_exists(value, sep=','):
    """Соединяет список в строку через sep, если список не пустой"""
    if value:
        return sep.join(map(str, value))
    return ''