"""
Abilities allow Actors to perform Actions and ask Questions.
"""


from .authenticate_with_2fa import AuthenticateWith2FA
from .browse_the_web import BrowseTheWeb

__all__ = [
    "AuthenticateWith2FA",
    "BrowseTheWeb",
]
