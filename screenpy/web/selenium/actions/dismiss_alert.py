"""
Dismiss a javascript alert.
"""

from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.core.actor import Actor
from screenpy.core.pacing import aside, beat


class DismissAlert:
    """Dismiss an alert.

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.attempts_to(DismissAlert())
    """

    @beat("{} dismisses the alert.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to dismiss the alert."""
        browser = the_actor.uses_ability_to(BrowseTheWeb).browser
        alert = browser.switch_to.alert
        aside(f'... the alert says "{alert.text}"')
        alert.dismiss()
