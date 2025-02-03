from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
    LoginUser,
    logout_user,
)

app_name = 'users'

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    # path('logout/', LogoutView.as_view(http_method_names = ['get', 'post', 'options']), name='logout'),
]
