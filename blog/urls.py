# blog/urls.py

# Django modules
from django.urls import path

# Locals
from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
]
