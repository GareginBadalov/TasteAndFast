from django import template
from showcase.models import *

register = template.Library()


@register.simple_tag(name='getrubs')
def get_rubrics():
    return Rubrics.objects.all()


@register.simple_tag(name='getrests')
def get_restaurants():
    return Restaurants.objects.all()


@register.inclusion_tag("rubrics")
def show_rubrics():
    rubrics = Rubrics.objects.all()
    return {"rubs": rubrics}
