from django import template
import recipeapp.views as views

register = template.Library()


@register.simple_tag()
def get_category():
    return views.category_db
