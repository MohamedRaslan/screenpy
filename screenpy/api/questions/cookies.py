"""
Investigate the cookies on the Actor's web or API session.
"""

from screenpy.core import Actor
from screenpy.api.abilities import MakeAPIRequests
from screenpy.core.exceptions import UnableToAnswer
from screenpy.core.pacing import beat


class Cookies:
    """Ask about the cookies on the Actor's session.

    This can be either an API session or their browsing session, whichever one
    they have. If they have both, use one of the more specific Questions,
    |CookiesOnTheAPISession|, directly.

    Abilities Required:
        |MakeAPIRequests|

    Examples::

        the_actor.should(
            See.the(Cookies(), ContainTheEntry(type="chocolate chip"))
        )
    """

    def answered_by(self, the_actor: Actor) -> dict:
        """Direct the Actor to investigate their cookies."""
        if the_actor.has_ability_to(MakeAPIRequests):
            return CookiesOnTheAPISession().answered_by(the_actor)

        raise UnableToAnswer(f"{the_actor} has no cookies!")


class CookiesOnTheAPISession:
    """Ask about the cookies on the Actor's API session.

    Abilities Required:
        |MakeAPIRequests|

    Examples::

        the_actor.should(
            See.the(CookiesOnTheAPISession(), ContainTheEntry(type="snickerdoodle"))
        )
    """

    @beat("{} inspects their API session's cookies.")
    def answered_by(self, the_actor: Actor) -> dict:
        """Direct the Actor to investigate their API session's cookies."""
        cookies = the_actor.uses_ability_to(MakeAPIRequests).session.cookies
        return cookies.get_dict()
