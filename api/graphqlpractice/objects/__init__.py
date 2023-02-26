from . import (
    author,
    post,
)

from .author import *
from .post import *

__all__ = (
    list(author.__all__)
    + list(post.__all__)
)