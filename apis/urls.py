from django.urls import path
from . import views

app_name = 'apis'

urlpatterns = [
    path('firstapi/', views.firstapi)
]