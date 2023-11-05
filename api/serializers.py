from rest_framework import serializers
from api.models import Book

# Define a shared publication year validation function.
def validate_publication_year(value):
    if value < 1700 or value > 2023:
        raise serializers.ValidationError("Publication year must be between 1700 and 2023.")

# Define serializers for the 'Book' model.
class BookSerializer(serializers.HyperlinkedModelSerializer):
     # A read-only field for 'company_id' which is not editable through this serializer.
    company_id = serializers.ReadOnlyField()
    
    class Meta:
        model = Book
        fields = "__all__" # Include all fields of the 'Book' model.
        
    # Validate the 'publication_year' field using the shared validation function.
    publication_year = serializers.IntegerField(
        validators=[validate_publication_year]
    )

    # Ensure the 'genre' field is required/not Empty when created
    # Ensure the 'genre' field is required/not Empty when created
    genre = serializers.CharField(
        required=True
    )

# Serializer for partial updates to the 'Book' model.
class BookPartialUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Book
        # Include only selected fields for partial updates.
        fields = ['genre', 'publication_year']
    
    # Validate the 'publication_year' field using the shared validation function.
    publication_year = serializers.IntegerField(
        validators=[validate_publication_year]
    )

    # Ensure the 'genre' field is required/not Empty for partial updates.
    genre = serializers.CharField(
        required=True
    )