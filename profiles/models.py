from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User


# Model to represent a user profile
class Profile(models.Model):
    # One-to-one relationship with the User model
    owner = models.OneToOneField(User, on_delete=models.CASCADE)

    # Timestamp for when the profile was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Timestamp for when the profile was last updated
    updated_at = models.DateTimeField(auto_now=True)

    # Name field for the profile, can be blank
    name = models.CharField(max_length=255, blank=True)

    # Content field for additional profile information, can be blank
    content = models.TextField(blank=True)

    # Image field for the profile picture, with a default image
    image = models.ImageField(
        upload_to='images/', default='../default_profile_jbayvj'
    )

    # Meta class to define model options
    class Meta:
        # Order profiles by creation date in descending order
        ordering = ['-created_at']

    # String representation of the Profile model
    def __str__(self):
        return f"{self.owner}'s profile"


# Function to create a profile when a new user is created
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance)


# Connect the create_profile function to the post_save signal of the User model
post_save.connect(create_profile, sender=User)
