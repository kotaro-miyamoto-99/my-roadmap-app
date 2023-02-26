import graphene

from .objects import Author, Post
from app.repositories import AuthorRepository, PostRepository

__all__ = ["QueryRoot"]


class QueryRoot(graphene.ObjectType):
    authors = graphene.List(Author)
    posts = graphene.List(Post)
    def resolve_authors(self, info):
        return AuthorRepository.all()

    def resolve_posts(self, info):
        return PostRepository.all()