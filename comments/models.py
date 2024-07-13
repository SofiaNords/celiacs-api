from django.db import models
from django.contrib.auth.models import User
from posts.models import Post


class Comment(models.Model):
    # ForeignKey to the User model, representing the owner of the comment
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    # ForeignKey to the Post model
    # representing the post the comment is related to
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    # DateTimeField to store the creation time of the comment
    created_at = models.DateTimeField(auto_now_add=True)

    # DateTimeField to store the last update time of the comment
    updated_at = models.DateTimeField(auto_now=True)

    # TextField to store the content of the comment
    content = models.TextField()

    class Meta:
        # Order comments by creation time in descending order
        ordering = ['-created_at']

    def __str__(self):
        # Return the content of the comment as its string representation
        return self.content
