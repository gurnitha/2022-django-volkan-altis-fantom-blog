# blog/urls.py

# Django modules
from django.urls import path

# Locals
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', HomePageView.as_view(), name='index'),
]
