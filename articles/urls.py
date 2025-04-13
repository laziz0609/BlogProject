from django.urls import path
from .views import ArticleListView , ArticleDetailView , ArticleUpdateView , ArticleDeleteView , ArticleCreateView
urlpatterns = [
  path('', ArticleListView.as_view(), name='article_list'),
  path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
  path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article_update'),
  path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article_delete'),
  path('article/create/', ArticleCreateView.as_view(), name='article_create'),

]