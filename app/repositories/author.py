from app.models import Author
from app.repositories.repository import Repository

__all__ = ["AuthorRepository"]

class AuthorRepository(Repository):
    cls = Author

    @staticmethod
    def all():
        return Author.objects.all()

    @staticmethod
    def create(author) -> Author:
        return author.save()