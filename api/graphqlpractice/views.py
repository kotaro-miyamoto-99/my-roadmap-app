from django.conf import settings
from graphene_django.views import GraphQLView

from .schema import schema

__all__ = ["view"]

view: GraphQLView = GraphQLView.as_view(
    schema = schema, graphiql = settings.DEBUG
)