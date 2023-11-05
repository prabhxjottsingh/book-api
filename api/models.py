from django.db import models

# Define the 'Book' model class, which represents a book entity in the database.
# This class inherits from the 'models.Model' class, making it a Django model.
class Book(models.Model):
    # Primary key for the 'Book' model, auto-incrementing
    book_id = models.AutoField(primary_key=True)

    # Title of the book, limited to 100 characters.
    title = models.CharField(max_length=100)

    # Author of the book, limited to 100 characters.
    author = models.CharField(max_length=100)

    # Genre of the book, limited to 100 characters.
    genre = models.CharField(max_length=100)

    # Year of publication for the book.
    publication_year = models.IntegerField()

    # Date and time when the book was added, automatically set to the current date and time.
    added_date = models.DateTimeField(auto_now_add=True)
