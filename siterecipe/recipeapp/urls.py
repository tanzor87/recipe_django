from django.urls import path, include
from .views import (
    RecipeIndexView,
    AboutView,
    addrecipe,
    login,
    show_detail,
)

urlpatterns = [
    path('', RecipeIndexView.as_view(), name='home'),
    path('about/', AboutView.as_view(), name='about'),
    path('addrecipe/', addrecipe, name='add_recipe'),
    path('login/', login, name='login'),
    path('detail/<int:detail_id>/', show_detail, name='detail')
]