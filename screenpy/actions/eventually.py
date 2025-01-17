"""
Eventually perform a Task or Action, trying until a set timeout.
"""

import time
from typing import TYPE_CHECKING, Optional

from screenpy import settings
from screenpy.pacing import the_narrator
from screenpy.protocols import Performable

if TYPE_CHECKING:
    from screenpy import Actor


class Eventually:
    """Retry a performable that will eventually (hopefully) succeed.

    ``Eventually`` ignores all errors for the duration of its attempt. If the
    Actor is not able to complete the given Action or Task within the timeout
    period, a TimeoutError and the last caught exception are raised.

    Examples::

        the_actor.should(
            Eventually(
                See.the(Text.of_the(WELCOME_BANNER), ContainsTheText("Welcome!"))
            ),
        )

        the_actor.attempts_to(
            Eventually(Click.on_the(BUTTON)).trying_every(100).milliseconds())

        the_actor.was_able_to(
            Eventually(
                DismissAlert()
            ).trying_for(5).seconds().polling_every(500).milliseconds(),
        )
    """

    performable: Performable
    caught_error: Optional[Exception]
    timeout: float

    class _TimeframeBuilder:
        """
        Allows caller of Eventually to tack on waiting for specific time
        frames in seconds or milliseconds.
        """

        def __init__(
            self, eventually: "Eventually", amount: float, attribute: str
        ) -> None:
            self.eventually = eventually
            self.amount = amount
            self.attribute = attribute
            self.eventually.timeout = amount

        def milliseconds(self) -> "Eventually":
            """Set the timeout in milliseconds."""
            setattr(self.eventually, self.attribute, self.amount / 1000)
            return self.eventually

        millisecond = milliseconds

        def seconds(self) -> "Eventually":
            """Set the timeout in seconds."""
            setattr(self.eventually, self.attribute, self.amount)
            return self.eventually

        second = seconds

        def perform_as(self, the_actor: "Actor") -> None:
            """Just in case the author forgets to use a unit method."""
            the_actor.attempts_to(self.eventually)

    def for_(self, amount: float) -> _TimeframeBuilder:
        """Set for how long the actor should continue trying."""
        return self._TimeframeBuilder(self, amount, "timeout")

    trying_for_no_longer_than = trying_for = waiting_for = for_

    def polling(self, amount: float) -> _TimeframeBuilder:
        """Adjust the polling frequency."""
        self.poll = amount
        return self._TimeframeBuilder(self, amount, "poll")

    trying_every = polling_every = polling

    def perform_as(self, the_actor: "Actor") -> None:
        """Direct the actor to just keep trying."""
        if self.poll > self.timeout:
            raise ValueError("poll must be less than or equal to timeout")

        end_time = time.time() + self.timeout

        with the_narrator.mic_cable_kinked():
            while True:
                the_narrator.clear_backup()
                try:
                    the_actor.attempts_to(self.performable)
                    return
                except Exception as exc:  # pylint: disable=W0703
                    self.caught_error = exc

                time.sleep(self.poll)
                if time.time() > end_time:
                    break

        msg = (
            f"{the_actor} used Eventually for {self.timeout} seconds,"
            f" but got: {self.caught_error}"
        )
        raise TimeoutError(msg) from self.caught_error

    def __init__(self, performable: Performable):
        self.performable = performable
        self.caught_error = None
        self.timeout = settings.TIMEOUT
        self.poll = 0.5
