"""
An action to set the headers on an API request.
"""

from screenpy import Actor
from screenpy.abilities import MakeAPIRequests
from screenpy.pacing import aside, beat


class SetHeaders:
    """Set the headers of your API requests to this specific set.

    Note this will remove all other headers on your requests.

    Abilities Required:
        |MakeAPIRequests|

    Examples::

        the_actor.attempts_to(SetHeaders(Cookies="csrf_token=1234"))

        the_actor.attempst_to(SetHeaders.to(Cookies="csrf_token=1234"))
    """

    @staticmethod
    def to(**kwargs: str) -> "SetHeaders":
        """Specify the headers to set."""
        return SetHeaders(**kwargs)

    def which_should_be_kept_secret(self) -> "SetHeaders":
        """Indicate these headers should not be written to the log."""
        self.secret = True
        self.secret_log = " secret"
        return self

    secretly = which_should_be_kept_secret

    @beat("{} sets the{secret_log} headers of their session.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the actor to set the headers for their requests."""
        if not self.secret:
            aside(f"... the headers are:\n{self.headers}")
        session = the_actor.ability_to(MakeAPIRequests).session
        session.headers.clear()
        session.headers.update(self.headers)

    def __init__(self, **kwargs: str) -> None:
        self.headers = kwargs
        self.secret = False
        self.secret_log = ""
