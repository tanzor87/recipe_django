from django.http import HttpRequest, HttpResponse, HttpResponseNotFound
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, FormView, CreateView, UpdateView

from .forms import AddRecipeForm, UploadImageForm
from .models import Ingredients, RecipeBase, Category, Composition, UploadFiles
from .utils import DataMixin


class RecipeIndexView(DataMixin, ListView):
    template_name = 'recipeapp/recipe-index.html'
    context_object_name = 'recipe'
    title_page = 'Главная'
    category_selected = 0
    paginate_by = 3

    def get_queryset(self):
        return RecipeBase.objects.all()


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


class AddRecipe(DataMixin, CreateView):
    form_class = AddRecipeForm
    template_name = 'recipeapp/addrecipe.html'
    title_page = 'Добавление рецепта'


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
    paginate_by = 3

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
