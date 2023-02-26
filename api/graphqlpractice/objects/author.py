from app.models import Author as AuthorModel
from graphene_django import DjangoObjectType

__all__ = ["Author"]

class Author(DjangoObjectType):
    class Meta:
        model = AuthorModel