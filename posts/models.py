from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    # ForeignKey to the User model, representing the owner of the post
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # DateTimeField to store the creation time of the post
    created_at = models.DateTimeField(auto_now_add=True)

    # DateTimeField to store the last update time of the post
    updated_at = models.DateTimeField(auto_now=True)

    # CharField to store the title of the post
    title = models.CharField(max_length=255)

    # CharField to store the location related to the post
    location = models.CharField(max_length=255)

    # TextField to store the content of the post, can be blank
    content = models.TextField(blank=True)

    # ImageField to store the image related to the post
    # with a default image and can be blank
    image = models.ImageField(
        upload_to='images/', default='../default_post_ptvomy', blank=True
    )

    class Meta:
        # Order posts by creation time in descending order
        ordering = ['-created_at']

    def __str__(self):
        # Return the ID and title of the post as its string representation
        return f'{self.id} {self.title}'
