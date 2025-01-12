from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Ingredients, RecipeBase

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    {'title': 'Войти', 'url_name': 'login'},
]

date_db = [
    {'id': 1, 'title': 'Салат с курицей и корейской морковкой',
     'content': """Сытный и очень вкусный праздничный салат с отварным куриным филе, жареными шампиньонами и морковью по-корейски. Салат легкий и достаточно быстрый в приготовлении. """,
     'products': ['Филе куриное', 'Шампиньоны маленькие', 'Лук репчатый', 'Морковь по-корейски', 'Яйца', 'Сыр твердый',
                  'Майонез', 'Масло растительное', 'Соль', 'Перец черный молотый'], 'recipe': {
        1: """Подготовьте все необходимые продукты. Куриную грудку отварите в кипящей воде до готовности - минут 15-20. Яйца отварите вкрутую (8 минут), остудите в холодной воде.""",
        2: """Нарежьте лук полукольцами. Грибы нарежьте небольшим кубиком.""",
        3: """Обжарьте лук и грибы на небольшом огне в минимальном количестве растительного масла.""",
        4: """Готовую куриную грудку остудите, нарежьте тонкими ломтиками.""",
        5: """Вареные яйца очистите от скорлупы, порубите ножом.""",
        6: """Натрите на крупной терке твердый сыр.""",
        7: """Сложите все ингредиенты в глубокую миску, добавьте морковь. Посолите салат, поперчите по вкусу, добавьте майонез.""",
        8: """Перемешайте салат и дайте ему несколько минут настояться перед подачей.""",
        9: """Готовый салат с курицей, грибами и морковью по-корейски подавайте сразу же после приготовления."""}},

    {'id': 2, 'title': 'Салат "Ёжик"',
     'content': """Этот сытный салат с колбасой, сыром и кукурузой подойдёт к любому празднику. """,
     'products': ['Колбаса копченая', 'Сыр твердый', 'Кукуруза консервированная', 'Яйца вареные', 'Чеснок ', 'Майонез'],
     'recipe': {
         1: """Подготовить продукты. Яйца заранее сварить вкрутую (10 минут) и остудить в холодной воде. """,
         2: """Колбасу нарезать кубиками. """,
         3: """Яйца нарезать кубиками. """,
         4: """Сыр натереть на тёрке. """,
         5: """Соединить колбасу, сыр, яйца и кукурузу (без жидкости). """,
         6: """Чеснок очистить и выдавить через чеснокодавилку. """,
         7: """Заправить салат "Ежик" майонезом и перемешать все ингредиенты. """,
         8: """Приятного аппетита! """,
     }
     },
    {'id': 3,
     'title': 'Салат "Красное море"',
     'content': """Гости на пороге. Что делать? Салат "Красное море" готовится всего за 10 минут, и гости будут в удивлении и в восторге:) Быстро, вкусно и красиво. """,
     'products': ['Крабовые палочки', 'Помидоры', 'Сыр', 'Чеснок', 'Соль', 'Майонез'],
     'recipe': {
         1: """Продукты для салата "Красное море" перед вами. """,
         2: """Как приготовить салат "Красное море": Сыр твердый натереть на крупной терке. """,
         3: """Помыть и нарезать помидоры соломкой. """,
         4: """Крабовые палочки нарезать тонкими колечками. """,
         5: """Чеснок очистить и мелко нарезать ножом.""",
         6: """Все продукты соединить в миске. Посолить по вкусу. """,
         7: """Салат "Красное море" заправить майонезом. """,
         8: """Хорошо перемешать салат. """,
         9: """ Салат "Красное море" готов. Приятного аппетита! """
     }
     },
]

category_db = [
    {'id': 1, 'name': 'Первые блюда'},
    {'id': 2, 'name': 'Вторые блюда'},
    {'id': 3, 'name': 'Салаты'},
]


class RecipeIndexView(View):

    def get(self, request: HttpRequest) -> HttpResponse:
        recipes = RecipeBase.objects.all()

        context = {
            'title': 'Главная',
            'menu': menu,
            # 'posts': date_db,
            'recipe': recipes,
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


def show_category(request: HttpRequest, category_id) -> HttpResponse:
    context = {
        'title': 'Главная',
        'menu': menu,
        'posts': date_db,
        'category_selected': category_id,
    }
    return render(request, 'recipeapp/recipe-index.html', context=context)


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
