from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse


def translit_to_eng(s: str) -> str:
    d = {'а': 'a', 'б': 'b', 'в': 'v', 'г': 'g', 'д': 'd',
         'е': 'e', 'ё': 'yo', 'ж': 'zh', 'з': 'z', 'и': 'i', 'к': 'k',
         'л': 'l', 'м': 'm', 'н': 'n', 'о': 'o', 'п': 'p', 'р': 'r',
         'с': 's', 'т': 't', 'у': 'u', 'ф': 'f', 'х': 'h', 'ц': 'c', 'ч': 'ch',
         'ш': 'sh', 'щ': 'shch', 'ь': '', 'ы': 'y', 'ъ': '', 'э': 'r', 'ю': 'yu', 'я': 'ya'}

    return "".join(map(lambda x: d[x] if d.get(x, False) else x, s.lower()))


class UnitMeasure(models.Model):
    unit_measure_name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.unit_measure_name


class Ingredients(models.Model):
    ingredient_name = models.CharField(max_length=255, unique=True, verbose_name='Ингредиент')

    class Meta:
        ordering = ['ingredient_name']

    def __str__(self):
        return self.ingredient_name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_slug': self.slug})


class RecipeBase(models.Model):
    recipe_title = models.CharField(max_length=255, verbose_name='Название рецепта')
    photos = models.ImageField(upload_to='photos/%Y/%m/%d',
                               default=None,
                               blank=True,
                               null=True,
                               verbose_name='Изображение')
    short_description = models.TextField(blank=True, verbose_name='Короткое описание')
    cooking_description = models.TextField(blank=True, verbose_name='Пошаговый рецепт')
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, related_name='cat_recipe',
                                 verbose_name='Категория')
    recipe_ingredients = models.ManyToManyField(
        Ingredients,
        related_name='ingredients_recipe',
        through='Composition',
        verbose_name="Ингредиенты"
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        related_name='recipes',
        null=True,
        default=None,
        verbose_name="Автор")

    class Meta:
        ordering = ['recipe_title']

    def get_absolute_url(self):
        return reverse('detail', kwargs={'detail_id': self.pk})

    def __str__(self):
        return self.recipe_title


class Composition(models.Model):
    recipe = models.ForeignKey(RecipeBase, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredients, on_delete=models.CASCADE)
    unit_measurer = models.ForeignKey(UnitMeasure, on_delete=models.CASCADE, verbose_name='Единицы измерения')
    quantity = models.FloatField(verbose_name='Количество')

    def __str__(self):
        if (float(str(self.quantity))).is_integer() and self.quantity != 0.0:
            q = int(float(str(self.quantity)))
            result = f'{self.ingredient} - {q} {self.unit_measurer}'
        elif self.quantity == 0.0:
            result = f'{self.ingredient} - {self.unit_measurer}'
        else:
            result = f'{self.ingredient} - {self.quantity} {self.unit_measurer}'
        return result


class Category(models.Model):
    category_name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    category_slug = models.SlugField(max_length=100, unique=True, db_index=True, verbose_name='Slug')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        # ordering = ['category_name']

    def get_absolut_url(self):
        return reverse('category', kwargs={'category_slug': self.category_slug})

    def __str__(self):
        return self.category_name

    # def save(self, *args, **kwargs):
    #     self.category_slug = slugify(translit_to_eng(self.category_name))
    #     super().save(*args, **kwargs)


class UploadFiles(models.Model):
    file = models.FileField(upload_to='uploads_model')
