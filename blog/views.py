# blog/views.py

# Django modules
from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.


class HomePageView(TemplateView):
    template_name = "blog/index.html"





