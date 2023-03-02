from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from . import graphqlpractice

urlpatterns = [
    path(
        "graphqlpractice/graphql",
        csrf_exempt(graphqlpractice.view),
        name="graphqlpractice-graphql"
    ),
]