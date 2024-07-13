from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


# Model to represent a selection made by a user on a post
class Select(models.Model):
    # Foreign key relationship to the User model
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # Foreign key relationship to the Post model, with a related name 'select'
    post = models.ForeignKey(
        Post, related_name='select', on_delete=models.CASCADE
    )
    # Timestamp for when the selection was created
    created_at = models.DateTimeField(auto_now_add=True)

    # Meta class to define model options
    class Meta:
        # Order selections by creation date in descending order
        ordering = ['-created_at']
        # Ensure that each user can only select a post once
        unique_together = ['owner', 'post']

    # String representation of the Select model
    def __str__(self):
        return f'{self.owner} {self.post}'
