from rest_framework import serializers
from .models import Author,Book


class AuthorSerializer(serializers.ModelSerializer):

 class Meta:
   
    model = Author
    fiels = '__all__'


class BookSerializer(serializers.ModelSerializer):

 class Meta:
   
    model = Book
    fiels = '__all__'

    