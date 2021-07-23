"""
API test example that tests cookies.
"""

from screenpy.core import Actor, then, when
from screenpy.core.actions import SeeAllOf
from screenpy.api.actions import SendGETRequest
from screenpy.api.questions import Cookies, StatusCodeOfTheLastResponse
from screenpy.core.resolutions import ContainTheEntry, IsEqualTo

from ..urls import SET_COOKIES_URL


def test_set_cookies(Perry: Actor) -> None:
    """Cookies set by the set cookies endpoint appear on the session."""
    test_cookie = {"type": "macaroon"}

    when(Perry).attempts_to(
        SendGETRequest.to(SET_COOKIES_URL).with_(params=test_cookie)
    )

    then(Perry).should(
        SeeAllOf.the(
            (StatusCodeOfTheLastResponse(), IsEqualTo(200)),
            (Cookies(), ContainTheEntry(**test_cookie)),
        )
    )
