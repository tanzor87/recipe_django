from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import formset_factory
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddRecipeForm, UploadImageForm
from .models import Ingredients, RecipeBase, Category, Composition, UploadFiles, UnitMeasure
from .utils import DataMixin

menu = [
    {'title': 'О сайте', 'url_name': 'about'},
    {'title': 'Добавить рецепт', 'url_name': 'add_recipe'},
    # {'title': 'Войти', 'url_name': 'login'},
]


class RecipeIndexView(DataMixin, ListView):
    template_name = 'recipeapp/recipe-index.html'
    context_object_name = 'recipe'
    title_page = 'Главная'
    category_selected = 0
    paginate_by = 5

    def get_queryset(self):
        return RecipeBase.objects.all()


def about(request: HttpRequest) -> HttpResponse:
    context = {
        'title': 'О сайте',
        'menu': menu,
    }
    return render(request, 'recipeapp/about.html', context=context)


class ShowDetail(DataMixin, DetailView):
    template_name = 'recipeapp/details.html'
    pk_url_kwarg = 'detail_id'
    context_object_name = "recipe"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return self.get_mixin_context(
            context,
            composition=Composition.objects.filter(recipe_id=self.kwargs['detail_id']),
            title=context['recipe'].recipe_title,
        )

    def get_object(self, queryset=None):
        return get_object_or_404(RecipeBase, id=self.kwargs[self.pk_url_kwarg])


@login_required
def add_recipe(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        ingredient_names = request.POST.getlist('ingredient_name')
        quantities = request.POST.getlist('quantity')
        unit_measures = request.POST.getlist('unit_measure')

        if recipe_form.is_valid():
            recipe = recipe_form.save(commit=False)
            recipe.author = request.user
            recipe.save()

            for ingredient_name, quantity, unit_measure_name in zip(ingredient_names, quantities, unit_measures):
                ingredient, created = Ingredients.objects.get_or_create(ingredient_name=ingredient_name)
                unit_measure, created = UnitMeasure.objects.get_or_create(unit_measure_name=unit_measure_name)
                composition = Composition(recipe=recipe, ingredient=ingredient, quantity=quantity,
                                          unit_measurer=unit_measure)
                composition.save()

            return redirect('home')
    else:
        recipe_form = AddRecipeForm()

    context = {
        'menu': menu,
        'title': 'Добавление рецепта',
        'recipe_form': recipe_form,
    }
    return render(request, 'recipeapp/addrecipe.html', context=context)


class UpdateRecipe(DataMixin, UpdateView):
    model = RecipeBase
    fields = ['recipe_title', 'photos', 'short_description', 'cooking_description', 'category']
    template_name = 'recipeapp/addrecipe.html'
    title_page = 'Редактирование рецепта'


class RecipeCategory(DataMixin, ListView):
    template_name = 'recipeapp/recipe-index.html'
    context_object_name = 'recipe'
    allow_empty = False
    paginate_by = 5

    def get_queryset(self):
        query = RecipeBase.objects.filter(category__category_slug=self.kwargs['category_slug'])
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category = context['recipe'][0].category

        return self.get_mixin_context(
            context,
            title='Категория - ' + category.category_name,
            category_selected=category.pk
        )


def page_not_found(request: HttpRequest, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
