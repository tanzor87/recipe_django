from django import forms
from .models import Category, Ingredients, Composition, RecipeBase


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
        fields = '__all__'
        # fields = ['recipe_title', 'photos', 'short_description', 'cooking_description', 'category']
        widgets = {
            'recipe_title': forms.TextInput(attrs={'class': 'form-input'}),
            'short_description': forms.Textarea(attrs={'cols': 50, 'rows': 5}),
            'cooking_description': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }


class UploadImageForm(forms.Form):
    file = forms.ImageField(label='Изображение')




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