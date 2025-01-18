from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Ingredients, RecipeBase, Category

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    {'title': 'Войти', 'url_name': 'login'},
]

class RecipeIndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        recipes = RecipeBase.objects.all()

        context = {
            'title': 'Главная',
            'menu': menu,
            'recipe': recipes,
            'category_selected': 0,
        }
        return render(request, 'recipeapp/recipe-index.html', context=context)


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'title': 'О сайте',
            'menu': menu,
        }
        return render(request, 'recipeapp/about.html', context=context)


def show_detail(request: HttpRequest, detail_id) -> HttpResponse:
    recipe = get_object_or_404(RecipeBase, pk=detail_id)

    context = {
        'title': 'Рецепт',
        'menu': menu,
        'recipe': recipe,
        'recipe_selected': 1,
    }

    return render(request, 'recipeapp/details.html', context=context)


def addrecipe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Добавление рецепта")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


def show_category(request: HttpRequest, category_slug) -> HttpResponse:
    category = get_object_or_404(Category, category_slug=category_slug)
    recipe_category = RecipeBase.objects.filter(category_id=category.pk)
    print(f'category = {category}')
    print(f'category name = {category.category_name}')
    print(f'PK = {category.pk}')
    context = {
        'title': f'Категория: {category.category_name}',
        'menu': menu,
        'recipe': recipe_category,
        'category_selected': category.pk,
    }
    return render(request, 'recipeapp/recipe-index.html', context=context)


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
