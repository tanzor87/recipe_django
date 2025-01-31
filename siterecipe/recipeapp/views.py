from lib2to3.fixes.fix_input import context

from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import TemplateView, ListView

from .forms import AddRecipeForm, UploadImageForm
from .models import Ingredients, RecipeBase, Category, Composition, UploadFiles

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    {'title': 'Войти', 'url_name': 'login'},
]


# class RecipeIndexView(View):
#
#     def get(self, request: HttpRequest) -> HttpResponse:
#         recipes = RecipeBase.objects.all()
#
#         context = {
#             'title': 'Главная',
#             'menu': menu,
#             'recipe': recipes,
#             'category_selected': 0,
#         }
#         return render(request, 'recipeapp/recipe-index.html', context=context)

class RecipeIndexView(TemplateView):
    template_name = 'recipeapp/recipe-index.html'
    recipes = RecipeBase.objects.all()
    extra_context = {
        'title': 'Главная',
        'menu': menu,
        'recipe': recipes,
        'category_selected': 0,
    }




def about(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            fp = UploadFiles(file=form.cleaned_data['file'])
            fp.save()
    else:
        form = UploadImageForm()

    context = {
        'title': 'О сайте',
        'menu': menu,
        'form': form,
    }
    return render(request, 'recipeapp/about.html', context=context)


def show_detail(request: HttpRequest, detail_id) -> HttpResponse:
    recipe = get_object_or_404(RecipeBase, pk=detail_id)
    composition = Composition.objects.filter(recipe_id=recipe)
    print(composition)

    context = {
        'title': 'Рецепт',
        'menu': menu,
        'recipe': recipe,
        'composition': composition,
        'recipe_selected': 1,
    }

    return render(request, 'recipeapp/details.html', context=context)


def addrecipe(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            # print(form.cleaned_data)
            # try:
            #     RecipeBase.objects.create(**form.cleaned_data)
            #     return redirect('home')
            # except:
            #     form.add_error(None, "Ошибка добавления рецепта")
            form.save()
            return redirect('home')
    else:
        form = AddRecipeForm()

    context = {
        'menu': menu,
        'title': 'Добавление рецепта',
        'form': form
    }
    return render(request, 'recipeapp/addrecipe.html', context=context)


class AddRecipe(View):
    def get(self, request):
        form = AddRecipeForm()
        context = {
            'menu': menu,
            'title': 'Добавление рецепта',
            'form': form
        }
        return render(request, 'recipeapp/addrecipe.html', context=context)

    def post(self, request):
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')

        context = {
            'menu': menu,
            'title': 'Добавление рецепта',
            'form': form
        }
        return render(request, 'recipeapp/addrecipe.html', context=context)


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

class RecipeCategory(ListView):
    template_name = 'recipeapp/recipe-index.html'
    context_object_name = 'recipe'
    allow_empty = False

    def get_queryset(self):
        query = RecipeBase.objects.filter(category__category_slug=self.kwargs['category_slug'])
        print(query)
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['recipe'][0].category
        context['title'] = 'Категория - ' + category.category_name
        context['menu'] = menu
        context['category_selected'] = category.pk
        print(context)
        return context




def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
