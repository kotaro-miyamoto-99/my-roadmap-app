import graphene
from .mutations import *

__all__ = ["Mutation"]

class Mutation(graphene.ObjectType):
    author_create = AuthorCreate.Field()