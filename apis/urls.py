from django.urls import path
from . import views
from .lib.get_users_api import Users

app_name = 'apis'

urlpatterns = [
    path('firstapi/', views.firstapi),
    path('get_users/', Users.as_view(), name="users")
]