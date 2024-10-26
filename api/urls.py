# from django.urls import path

from django.contrib import admin
from django.urls import include, path

from . import views
from .views import *
from django.conf import settings




urlpatterns = [
   
   path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
   path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
   path('books/', BookListCreateView.as_view(), name='book-list-create'),

   path('authors/<int:pk>/', BookDetailView.as_view(), name='book-detail'),

]