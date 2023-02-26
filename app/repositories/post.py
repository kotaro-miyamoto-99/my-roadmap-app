from app.models import Post
from app.repositories.repository import Repository

__all__ = ["PostRepository"]

class PostRepository(Repository):
    cls = Post

    @staticmethod
    def all():
        return Post.objects.all()