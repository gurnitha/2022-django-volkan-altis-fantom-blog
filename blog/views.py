# blog/views.py

# Django modules
from django.shortcuts import render
from django.utils import timezone
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
# Locals
from .models import Post 

# Create your views here.


class PostListView(ListView):

    model = Post 
    paginate_by = 2
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


class PostDetailView(DetailView):

    model = Post 
    context_object_name = 'post'
    template_name = "blog/post_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Post'
        return context





