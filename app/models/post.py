from django.db import models

from .author import Author

__all__ = ["Post"]

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(
        Author, related_name="posts", on_delete=models.CASCADE
    )
    def str(self):
        return self.title