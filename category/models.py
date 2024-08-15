from django.db import models

# Define a model for categories
class Category(models.Model):
    # Name of the category, must be unique and can have a maximum length of 50 characters
    name = models.CharField(max_length=50, unique=True)
    # Timestamp for when the category was created, automatically set when the object is created
    created_at = models.DateTimeField(auto_now_add=True)
    # Timestamp for when the category was last updated, automatically set whenever the object is saved
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
