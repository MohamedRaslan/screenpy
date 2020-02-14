"""
An action to select an item from a multi-selection field or dropdown. An
actor must possess the ability to BrowseTheWeb to perform this actin. An
actor can perform this action like so:

    the_actor.attempts_to(
        Select.the_option_named("January").from_the(MONTH_DROPDOWN)
    )

    the_actor.attempts_to(
        Select.the_option_at_index(0).from_the(MONTH_DROPDOWN)
    )

    the_actor.attempts_to(
        Select.the_option_with_value("jan").from_the(MONTH_DROPDOWN)
    )
"""


from typing import Optional, Union

from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support.ui import Select as SeleniumSelect

from ..actor import Actor
from ..exceptions import DeliveryError, UnableToActError
from ..pacing import beat
from ..target import Target
from .base_action import BaseAction


class Select:
    """
    Selects an option from a dropdown menu. This is an entry point that
    will create the correct specific Select action that will need to be
    used, depending on how the option needs to be selected. Some examples
    of invocations:

        Select.the_option_named("January").from_the(MONTH_DROPDOWN)
        Select.the_option_at_index(0).from_the(MONTH_DROPDOWN)
        Select.the_option_with_value("jan").from_the(MONTH_DROPDOWN)

    It can then be passed along to the |Actor| to perform the action.
    """

    @staticmethod
    def the_option_named(text: str) -> "SelectByText":
        """
        Instantiate a SelectByText class which will select the option with
        the given text.

        Args:
            text: the text of the option to select.

        Returns:
            |SelectByText|
        """
        return SelectByText(text)

    @staticmethod
    def the_option_at_index(index: Union[int, str]) -> "SelectByIndex":
        """
        Instantiate a SelectByIndex class which will select the option at
        the specified index. This index is 0-based.

        Args:
            index: the index (0-based) of the option to select.

        Returns:
            |SelectByIndex|
        """
        return SelectByIndex(index)

    @staticmethod
    def the_option_with_value(value: str) -> "SelectByValue":
        """
        Instantiate a SelectByText class which will select the option with
        the given text.

        Args:
            value: the value of the option to select.

        Returns:
            |SelectByText|
        """
        return SelectByValue(value)


class SelectByText(BaseAction):
    """
    A specialized Select action that chooses the option by text. This
    class is meant to be accessed via the Select action's static
    |Select.the_option_named| method. A typical invocation might look
    like:

        Select.the_option_named("January").from_the(MONTH_DROPDOWN)

    It can then be passed along to the |Actor| to perform the action.
    """

    target: Optional[Target]
    text: str

    def from_the(self, target: Target) -> "SelectByText":
        """
        Provides the target to select the option from.

        Args:
            target: the |Target| describing the dropdown or multi-select
                element to select the option from.

        Returns:
            |SelectByText|
        """
        self.target = target
        return self

    def from_(self, target: Target) -> "SelectByText":
        """Syntactic sugar for |SelectByText.from_the|."""
        return self.from_the(target)

    @beat("{0} selects the option '{text}' from the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor: The |Actor| who will perform the action.

        Raises:
            |DeliveryError|: an exception was raised by Selenium.
            |UnableToActError|: no target was supplied.
            |UnableToPerformError|: the actor does not have the ability to
                |BrowseTheWeb|.
        """
        if self.target is None:
            raise UnableToActError(
                "Target was not provided for SelectByText. Provide a target using the "
                ".from_() or .from_the() methods."
            )

        element = self.target.found_by(the_actor)
        select = SeleniumSelect(element)
        try:
            select.select_by_visible_text(self.text)
        except WebDriverException as e:
            msg = (
                "Encountered an issue while attempting to select the option with text "
                f"'{self.text}' from {self.target}: {e.__class__.__name__}"
            )
            raise DeliveryError(msg).with_traceback(e.__traceback__)

    def __init__(self, text: str, target: Optional[Target] = None) -> None:
        self.target = target
        self.text = text


class SelectByIndex(BaseAction):
    """
    A specialized |Select| action that chooses the option by its index.
    This class is meant to be accessed via the Select action's static
    |Select.the_option_at_index| method. A typical invocation might look
    like:

        Select.the_option_at_index(0).from_the(MONTH_DROPDOWN)

    It can then be passed along to the |Actor| to perform the action.
    """

    target: Optional[Target]
    index: str

    def from_the(self, target: Target) -> "SelectByIndex":
        """
        Provides the target to select the option from.

        Args:
            target: The |Target| describing the dropdown or multi-select
                 element to select the option from.

        Returns:
            |SelectByIndex|
        """
        self.target = target
        return self

    def from_(self, target: Target) -> "SelectByIndex":
        """Syntactic sugar for |SelectByIndex.from_the|."""
        return self.from_the(target)

    @beat("{0} selects the option at index {index} from the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor: The |Actor| who will perform the action.

        Raises:
            |DeliveryError|: an exception was raised by Selenium.
            |UnableToActError|: no target was supplied.
            |UnableToPerformError|: the actor does not have the ability to
                |BrowseTheWeb|.
        """
        if self.target is None:
            raise UnableToActError(
                "Target was not provided for SelectByIndex. Provide a target using the "
                ".from_() or .from_the() methods."
            )

        element = self.target.found_by(the_actor)
        select = SeleniumSelect(element)
        try:
            select.select_by_index(self.index)
        except WebDriverException as e:
            msg = (
                "Encountered an issue while attempting to select the option at index "
                f"{self.index} from {self.target}: {e.__class__.__name__}"
            )
            raise DeliveryError(msg).with_traceback(e.__traceback__)

    def __init__(self, index: Union[int, str], target: Optional[Target] = None) -> None:
        self.target = target
        self.index = str(index)


class SelectByValue(BaseAction):
    """
    A specialized Select action that chooses the option by its value. This
    class is meant to be accessed via the Select action's static
    |Select.the_option_with_value| method. A typical invocation might look
    like:

        Select.the_option_with_value("jan").from_the(MONTH_DROPDOWN)

    It can then be passed along to the |Actor| to perform the action.
    """

    target: Optional[Target]
    value: str

    def from_the(self, target: Target) -> "SelectByValue":
        """
        Provides the target to select the option from.

        Args:
            target: The |Target| describing the dropdown or multi-select
                element to select the option from.

        Returns:
            |SelectByValue|
        """
        self.target = target
        return self

    def from_(self, target: Target) -> "SelectByValue":
        """Syntactic sugar for |SelectByValue.from_the|."""
        return self.from_the(target)

    @beat("{0} selects the option with value '{value}' from the {target}.")
    def perform_as(self, the_actor: Actor) -> None:
        """
        Asks the actor to attempt to find the dropdown element described
        by the stored target, then performs the select action.

        Args:
            the_actor: The |Actor| who will perform the action.

        Raises:
            |DeliveryError|: an exception was raised by Selenium.
            |UnableToActError|: no target was supplied.
            |UnableToPerformError|: the actor does not have the ability to
                |BrowseTheWeb|.
        """
        if self.target is None:
            raise UnableToActError(
                "Target was not provided for SelectByValue. Provide a target using the "
                ".from_() or .from_the() methods."
            )

        element = self.target.found_by(the_actor)
        select = SeleniumSelect(element)
        try:
            select.select_by_value(self.value)
        except WebDriverException as e:
            msg = (
                "Encountered an issue while attempting to select the option with value "
                f"{self.value} from {self.target}: {e.__class__.__name__}"
            )
            raise DeliveryError(msg).with_traceback(e.__traceback__)

    def __init__(self, value: Union[int, str], target: Optional[Target] = None) -> None:
        self.target = target
        self.value = str(value)
