"""
Press the browser forward button.
"""

from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.core.actor import Actor
from screenpy.core.pacing import beat


class GoForward:
    """Press the browser forward button.

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.attempts_to(GoForward())
    """

    @beat("{} goes forward.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to press their browser's forward button."""
        browser = the_actor.ability_to(BrowseTheWeb).browser
        browser.forward()
