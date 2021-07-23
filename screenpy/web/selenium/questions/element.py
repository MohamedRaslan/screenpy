"""
Investigate an element on the browser page.
"""

from typing import Optional

from selenium.webdriver.remote.webelement import WebElement

from screenpy.core.actor import Actor
from screenpy.core.exceptions import TargetingError
from screenpy.core.pacing import beat
from screenpy.web.selenium.target import Target


class Element:
    """Ask to retrieve a specific element.

    Abilities Required:
        |BrowseTheWeb|

    Examples::

        the_actor.should(See.the(Element(WELCOME_BANNER), IsVisible()))
    """

    @beat("{} inspects the {target}.")
    def answered_by(self, the_actor: Actor) -> Optional[WebElement]:
        """Direct the Actor to find the element."""
        try:
            return self.target.found_by(the_actor)
        except TargetingError:
            return None

    def __init__(self, target: Target) -> None:
        self.target = target
