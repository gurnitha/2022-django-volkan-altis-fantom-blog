# blog/urls.py

# Django modules
from django.urls import path

# Locals
from .views import *

app_name = 'blog'
urlpatterns = [
    path('', PostListView.as_view(), name='post_list'),
]
