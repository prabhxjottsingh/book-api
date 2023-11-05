# Import necessary modules from Django and the project.
from django.shortcuts import render
from rest_framework import viewsets, generics
from api.models import Book
from api.serializers import BookSerializer, BookPartialUpdateSerializer

# Define a view set for the 'Book' model, inheriting from 'viewsets.ModelViewSet'.
class BookViewSet(viewsets.ModelViewSet):
    # Define the queryset to include all 'Book' objects.
    queryset = Book.objects.all()
    
    # Specify the serializer class for 'Book' objects.
    serializer_class = BookSerializer

# Define a view for partially updating 'Book' objects, inheriting from 'generics.UpdateAPIView'.
class BookPartialUpdateView(generics.UpdateAPIView):
    # Define the queryset to include all 'Book' objects.
    queryset = Book.objects.all()
    
    # Specify the serializer class for partial updates of 'Book' objects.
    serializer_class = BookPartialUpdateSerializer




