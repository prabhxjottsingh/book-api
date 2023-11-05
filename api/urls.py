# Import necessary modules from Django and the project's views.
from django.contrib import admin
from django.urls import path, include
from api.views import BookViewSet, BookPartialUpdateView
from rest_framework import routers

# Create a default router for handling API endpoints.
router = routers.DefaultRouter()
router.register('books', BookViewSet)

# Define URL patterns for the project.
urlpatterns = [
    # Include API endpoint routes provided by the 'api_router'.
    path('', include(router.urls)),
    
    # Define a custom URL pattern for partially updating a book using its primary key (pk).
    path('books/<int:pk>/partial-update/', BookPartialUpdateView.as_view(), name='book-partial-update'),
]