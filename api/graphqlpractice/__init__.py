from graphene import Schema
from .mutation import Mutation
from .query import QueryRoot
from .views import view

__all__ = ["schema", "view"]

schema = Schema(
    query=QueryRoot,
    mutation=Mutation,
)