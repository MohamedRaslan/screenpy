"""
Press the browser back button.
"""

from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.core.actor import Actor
from screenpy.core.pacing import beat


class GoBack:
    """Press the browser back button.

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.attempts_to(GoBack())
    """

    @beat("{} goes back.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to press their browser's back button."""
        browser = the_actor.ability_to(BrowseTheWeb).browser
        browser.back()
