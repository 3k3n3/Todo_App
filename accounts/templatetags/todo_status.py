from django import template

register = template.Library()

@register.filter
def status(value):
    return value.replace(" ", "_").lower()
