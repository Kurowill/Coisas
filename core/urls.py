from django.urls import path

from . import views

urlpatterns = [
    path('', views.BlogListView.as_view(), name='home'),
    path('post/new/', views.BlogCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.BlogDetaislView.as_view(), name='post_detail'), # Sempre que for trabalhar com slug deve-se manter essa pattern em ultimo
    path('post/<slug:slug>/edit/', views.BlogEditView.as_view(), name='post_edit'),

]