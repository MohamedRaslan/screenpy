"""
Actions are what the Actors do, possibly requiring use of their Abilities.
Ask your Actors to perform Actions by passing the Actions into their
|Actor.was_able_to| or |Actor.attempts_to| method.
"""

from .debug import Debug
from .make_note import MakeNote
from .see import See
from .see_all_of import SeeAllOf
from .see_any_of import SeeAnyOf

# Natural-language-enabling syntactic sugar
Observe = Verify = Confirm = Assert = See
ObserveAllOf = VerifyAllOf = ConfirmAllOf = AssertAllOf = SeeAllOf
ObserveAnyOf = VerifyAnyOf = ConfirmAnyOf = AssertAnyOf = SeeAnyOf
TakeNote = MakeNote


__all__ = [
    "Debug",
    "Observe",
    "ObserveAllOf",
    "ObserveAnyOf",
    "See",
    "SeeAllOf",
    "SeeAnyOf",
    "Verify",
    "VerifyAllOf",
    "VerifyAnyOf",
    "Visit",
    "Wait",
]
