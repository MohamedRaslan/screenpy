from .actor import Actor
from .director import Director
from .given_when_then import and_, given, given_that, then, when


# Natural-language-enabling syntactic sugar
AnActor = Actor


__all__ = [
    "Actor",
    "AnActor",
    "Director",
    "and_",
    "given",
    "given_that",
    "then",
    "when",
]
