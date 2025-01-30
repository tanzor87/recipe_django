from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import RecipeBase, Category


@admin.register(RecipeBase)
class RecipeAdmin(admin.ModelAdmin):
    fields = ['recipe_title', 'photos', 'recipe_photo',  'short_description', 'cooking_description', 'category']
    # filter_horizontal = ['recipe_ingredients']
    readonly_fields = ['recipe_photo']
    list_display = ('id', 'recipe_title', 'recipe_photo', 'short_description', 'time_update')
    list_display_links = ('id', 'recipe_title')
    ordering = ['time_update', 'recipe_title']
    list_per_page = 10
    search_fields = ['recipe_title']
    list_filter = ['category__category_name']


    @admin.display(description='Изображение', ordering='short_description')
    def recipe_photo(self, recipe: RecipeBase):
        if recipe.photos:
            return mark_safe(f"<img src='{recipe.photos.url}' width=50>")
        return 'Без фото'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # readonly_fields = ['category_slug']
    prepopulated_fields = {'category_slug': ('category_name', )}
    list_display = ('id', 'category_name')
    list_display_links = ('id', 'category_name')
    ordering = ['id']

# admin.site.register(RecipeBase, RecipeAdmin)
