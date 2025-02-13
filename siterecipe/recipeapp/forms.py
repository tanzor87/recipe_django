from django import forms
from django.forms import modelformset_factory

from .models import Category, Ingredients, Composition, RecipeBase, UnitMeasure


# class AddRecipeForm(forms.Form):
#     recipe_title = forms.CharField(
#         max_length=255,
#         label="Название рецепта",
#         error_messages={
#             'required': 'Без названия никак',
#         },
#         widget=forms.Textarea(attrs={'cols': 50, 'rows': 1}),
#     )
#     short_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 5}), label='Краткое описание')
#     cooking_description = forms.CharField(widget=forms.Textarea(attrs={'cols': 50, 'rows': 10}), label='Пошаговый рецепт')
#     category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана", label='Категория')

class AddRecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Категория не выбрана",
                                      label='Категория')

    # ingredient = forms.

    class Meta:
        model = RecipeBase
        # fields = '__all__'
        fields = ['recipe_title', 'photos', 'short_description', 'cooking_description', 'category']
        widgets = {
            'recipe_title': forms.TextInput(attrs={'class': 'form-input'}),
            'short_description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'cooking_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }


class UploadImageForm(forms.ModelForm):
    file = forms.ImageField(label='Изображение')


class IngredientForm(forms.ModelForm):
    class Meta:
        model = Ingredients
        fields = ['ingredient_name']


IngredientFormSet = modelformset_factory(Ingredients, fields=('ingredient_name',), extra=1)


class CompositionForm(forms.ModelForm):
    unit_measurer = forms.ModelChoiceField(queryset=UnitMeasure.objects.all(), empty_label="Не выбрана",
                                           label='Единица измерения')

    class Meta:
        model = Composition
        fields = ['quantity', 'unit_measurer']


CompositionFormSet = modelformset_factory(Composition, form=CompositionForm, extra=1)

# recipe_title = models.CharField(max_length=255, verbose_name='Название рецепта')
# short_description = models.TextField(blank=True, verbose_name='Короткое описание')
# cooking_description = models.TextField(blank=True)
# time_create = models.DateTimeField(auto_now_add=True)
# time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
# category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')
# recipe_ingredients = models.ManyToManyField(
#     Ingredients,
#     related_name='ingredients_recipe',
#     through='Composition',
# )
