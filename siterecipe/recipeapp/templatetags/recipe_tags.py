from django import template
from recipeapp.models import Category
import recipeapp.views as views

register = template.Library()


@register.inclusion_tag('recipeapp/list_categories.html')
def show_categories(category_selected_id=0):
    categories = Category.objects.all()
    return {'categories': categories, 'category_selected': category_selected_id}
