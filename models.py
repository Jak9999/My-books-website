from django.db import models  # Imports Django's built-in models module, which is used to define database models.


# Defines a model for Books
class Books(models.Model):
    # A CharField to store the name of the book, with a maximum length of 255 characters
    name = models.CharField(max_length=255)

    # A CharField to store the URL of the book's image, with a maximum length of 2083 characters
    image_url = models.CharField(max_length=2083)

    # A URLField to store the URL of the book's PDF, with a maximum length of 1024 characters
    pdf_url = models.URLField(max_length=1024)

    # String representation of the model, returns the book's name when the object is printed or displayed
    def __str__(self):
        return self.name


