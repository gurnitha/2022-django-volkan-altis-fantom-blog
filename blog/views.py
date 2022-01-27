# blog/views.py

# Django modules
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView

# Locals
from .models import Post 

# Create your views here.


class PostListView(ListView):

    model = Post 
    context_object_name = 'posts'
    template_name = "blog/index.html"

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        # context['now'] = timezone.now()
        context['title'] = 'Home'
        return context

    # Get all posts with status pubish
    def get_queryset(self):
        return self.model.objects.filter(status='published')





