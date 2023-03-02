from app.models import Post as PostModel
from graphene_django import DjangoObjectType

__all__ = ["Post"]

class Post(DjangoObjectType):
    class Meta:
        model = PostModel