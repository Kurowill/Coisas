from django.shortcuts import render

from django.views.generic import ListView, DetailView

from . models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'core/home.html'

class BlogDetaislView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    context_object_name = 'custom'