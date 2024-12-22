from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    try:
        return value * arg
    except (ValueError, TypeError):
        return ''
    
@register.filter
def replace(value, arg):
    """
    Replaces occurrences of `arg` in the `value` string with an empty string.
    """
    return value.replace(arg, "")