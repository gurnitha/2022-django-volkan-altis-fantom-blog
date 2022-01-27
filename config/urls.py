# config/urls.py

# Django modules
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Blog
    path('', include('blog.urls', namespace='blog')),
    # Admin
    path('admin/', admin.site.urls),
]
