from rest_framework  import generics
from .models import Author,Book
from .serializers import AuthorSerializer ,BookSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page




class AuthorListCreateView(generics.ListCreateAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class AuthorDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    

@method_decorator(cache_page(60*15), name='dispatch')
class BookListCreateView(generics.ListCreateAPIView):

    queryset = Book.objects.select_related('author').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['author__name','genre','published_date']
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
