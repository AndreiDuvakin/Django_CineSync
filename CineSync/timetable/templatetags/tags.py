from django import template

register = template.Library()


@register.filter(name='get_range')
def get_range(number):
    if number:
        return range(1, number + 1)

    return range(0)
