"""
Investigate the cookies on the Actor's web or API session.
"""

from screenpy.core import Actor
from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.core.exceptions import UnableToAnswer
from screenpy.core.pacing import beat


class Cookies:
    """Ask about the cookies on the Actor's session.

    This can be either an API session or their browsing session, whichever one
    they have. If they have both, use one of the more specific Questions,
    |CookiesOnTheAPISession| or |CookiesOnTheWebSession|, directly.

    Abilities Required:
        |BrowseTheWeb| or |MakeAPIRequests|

    Examples::

        the_actor.should(
            See.the(Cookies(), ContainTheEntry(type="chocolate chip"))
        )
    """

    def answered_by(self, the_actor: Actor) -> dict:
        """Direct the Actor to investigate their cookies."""
        if the_actor.has_ability_to(BrowseTheWeb):
            return CookiesOnTheWebSession().answered_by(the_actor)

        raise UnableToAnswer(f"{the_actor} has no cookies!")


class CookiesOnTheWebSession:
    """Ask about the cookies on the Actor's web browsing session.

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.should(
            See.the(CookiesOnTheWebSession(), ContainTheEntry(type="oatmeal raisin"))
        )
    """

    @beat("{} inspects their web browser's cookies...")
    def answered_by(self, the_actor: Actor) -> dict:
        """Direct the Actor to investigate their web browser's cookies."""
        cookies = the_actor.uses_ability_to(BrowseTheWeb).browser.get_cookies()
        return {c["name"]: c["value"] for c in cookies}
