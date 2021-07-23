"""
Accept a javascript alert.
"""

from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.core.actor import Actor
from screenpy.core.pacing import aside, beat


class AcceptAlert:
    """Accept an alert!

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.attempts_to(AcceptAlert())
    """

    @beat("{} accepts the alert.")
    def perform_as(self, the_actor: Actor) -> None:
        """Direct the Actor to accept the alert."""
        browser = the_actor.ability_to(BrowseTheWeb).browser
        alert = browser.switch_to.alert
        aside(f'... the alert says "{alert.text}"')
        alert.accept()
