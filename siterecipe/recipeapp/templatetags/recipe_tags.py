from django import template
from django.db.models import Count

from recipeapp.models import Category
from recipeapp.utils import menu

register = template.Library()


@register.simple_tag()
def get_menu():
    return menu


@register.inclusion_tag('recipeapp/list_categories.html')
def show_categories(category_selected_id=0):
    # categories = Category.objects.all()
    categories = Category.objects.annotate(total=Count('cat_recipe')).filter(total__gt=0)

    return {'categories': categories, 'category_selected': category_selected_id}
