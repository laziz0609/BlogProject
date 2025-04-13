from django.shortcuts import render
from django.views.generic import ListView , DetailView
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView , DeleteView , CreateView
from .models import Article

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(DetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleUpdateView(UpdateView):
    model = Article
    template_name = "article_update.html"
    fields = ['title', 'summary' , 'body' , 'photo']

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy('article_list')

class ArticleCreateView(CreateView):
    model = Article
    template_name = "article_create.html"
    fields = ['title', 'summary' , 'body' , 'photo' , 'author']
    success_url = reverse_lazy('article_list')

  