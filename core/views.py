from django.shortcuts import render

from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, UpdateView
from . models import Post

# Create your views here.

class BlogListView(ListView):
    model = Post
    template_name = 'core/home.html'

class BlogDetaislView(DetailView):
    model = Post
    template_name = 'core/post_detail.html'
    #context_object_name = 'custom' - exemplode como pode mudar esse nome do objeto para qualquer outro

class BlogCreateView(CreateView):
    model = Post
    template_name = 'core/post_new.html'
    fields = ('titulo','slug','conteudo','autor') # '__all__' - jeito de deixar todos os campos, mas pode-se utilizar apenas campos desejados

class BlogEditView(UpdateView):
    model = Post
    template_name = 'core/post_edit.html'
    fields = ('titulo','conteudo','autor')