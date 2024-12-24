from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.views import View


menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    {'title': 'Войти', 'url_name': 'login'},
]

class RecipeIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'title': 'Главная!',
            'menu': menu,
        }
        return render(request, 'recipeapp/recipe-index.html', context=context)


class AboutView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'title': 'О сайте'
        }
        return render(request, 'recipeapp/about.html', context=context)


def addrecipe(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Добавление рецепта")


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
