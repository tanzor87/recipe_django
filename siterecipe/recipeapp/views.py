from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddRecipeForm, UploadImageForm, IngredientForm, CompositionForm
from .models import Ingredients, RecipeBase, Category, Composition, UploadFiles
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

@login_required
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
        # 'menu': menu,
        'form': form,
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

class AddRecipe(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddRecipeForm
    template_name = 'recipeapp/addrecipe.html'
    title_page = 'Добавление рецепта'

    def form_valid(self, form):
        r = form.save(commit=False)
        r.author = self.request.user
        return super().form_valid(form)

# class AddRecipeView(LoginRequiredMixin, DataMixin, View):
#     title_page = 'Добавление рецепта'
#     def get(self, request):
#             form = AddRecipeForm()
#             context = {
#                 'form': form,
#             }
#             return render(request, 'recipeapp/addrecipe.html', context=context)

def add_recipe(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        recipe_form = AddRecipeForm(request.POST, request.FILES)
        ingredient_form = IngredientForm(request.POST, request.FILES)
        composition_form = CompositionForm(request.POST, request.FILES)
        print(ingredient_form)
        if all([recipe_form.is_valid(), ingredient_form.is_valid(), composition_form.is_valid()]):
            recipe = recipe_form.save()
            ingredient = ingredient_form.save(commit=False)
            if Ingredients.objects.filter(ingredient_name=ingredient).exists():
                print('мы зашли в условие')
                ingredient = Ingredients.objects.filter(ingredient_name=ingredient)
            else:
                # get_user_model().objects.filter(email=email).exists():
                print('мы НЕ зашли в условие')
                ingredient.save()
            composition = composition_form.save(commit=False)
            composition.recipe = recipe
            composition.ingredient = ingredient
            composition.save()

            return redirect('home')
    else:
        recipe_form = AddRecipeForm()
        ingredient_form = IngredientForm()
        composition_form = CompositionForm()

    context = {
        'menu': menu,
        'title': 'Добавление рецепта',
        'recipe_form': recipe_form,
        'ingredient_form': ingredient_form,
        'composition_form': composition_form,
    }
    return render(request, 'recipeapp/addrecipe.html', context=context)



class UpdateRecipe(DataMixin, UpdateView):
    model = RecipeBase
    fields = ['recipe_title', 'photos', 'short_description', 'cooking_description', 'category']
    template_name = 'recipeapp/addrecipe.html'
    title_page = 'Редактирование рецепта'


def login(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Авторизация")


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
