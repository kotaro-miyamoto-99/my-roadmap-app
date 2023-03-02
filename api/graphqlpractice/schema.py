from graphene import Schema

from .mutation import Mutation
from .query import QueryRoot

schema = Schema(query=QueryRoot, mutation=Mutation)