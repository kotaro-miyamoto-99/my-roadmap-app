from graphene import InputObjectType, String, Mutation, Field
from graphql import GraphQLResolveInfo
from typing import Any

from app.repositories import AuthorRepository
from app.models import Author as AuthorModel


from ..objects import Author

__all__ = ["AuthorCreate", "AuthorCreateInput"]





class AuthorCreateInput(InputObjectType):
    """
    入力受け取りクラス
    """
    name = String(required=True, description="作成者名")

class AuthorCreate(Mutation):
    """
    Author作成
    """
    class Arguments:
        input = AuthorCreateInput(required=True)
    author = Field(Author)

    @classmethod
    def mutate(cls, root:Any, info:GraphQLResolveInfo, input:AuthorCreateInput):
        try:
            author = AuthorModel(
                name = input.name
            )
            AuthorRepository.create(author)
            return AuthorCreate(author=author)
        except Exception as e:
            print(e)