from django.urls import path, include
from .views import (
    RecipeIndexView,
    about,
    add_recipe,
    UpdateRecipe,
    ShowDetail,
    RecipeCategory,
)

urlpatterns = [
    path('', RecipeIndexView.as_view(), name='home'),
    path('about/', about, name='about'),
    path('addrecipe/', add_recipe, name='add_recipe'),
    # path('addrecipe/', AddRecipe.as_view(), name='add_recipe'),
    path('edit/<int:pk>/', UpdateRecipe.as_view(), name='edit_recipe'),
    # path('login/', login, name='login'),
    # path('detail/<int:detail_id>/', show_detail, name='detail'),
    path('detail/<int:detail_id>/', ShowDetail.as_view(), name='detail'),
    # path('detail/<slug:detail_slug>/', show_detail, name='detail'),
    # path('category/<int:category_id>/', show_category, name='category'),
    # path('category/<slug:category_slug>/', show_category, name='category'),
    path('category/<slug:category_slug>/', RecipeCategory.as_view(), name='category'),
]