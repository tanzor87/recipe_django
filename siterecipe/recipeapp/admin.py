from django.contrib import admin
from .models import RecipeBase, Category


@admin.register(RecipeBase)
class RecipeAdmin(admin.ModelAdmin):
    # fields = ['recipe_title', 'short_description', 'cooking_description', 'category']
    # filter_horizontal = ['recipe_ingredients']
    list_display = ('id', 'recipe_title', 'short_description', 'time_update')
    list_display_links = ('id', 'recipe_title')
    ordering = ['time_update', 'recipe_title']
    list_per_page = 10
    search_fields = ['recipe_title']
    list_filter = ['category__category_name']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['category_slug']
    prepopulated_fields = {'category_slug': ('category_name', )}
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    ordering = ['id']

# admin.site.register(RecipeBase, RecipeAdmin)
