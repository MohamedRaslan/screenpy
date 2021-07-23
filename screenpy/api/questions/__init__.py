"""
Questions are asked by Actors to determine the actual value from the
current state of the application under test.

These form the first half of test assertions in Screenplay Pattern; the
second half is handled by Resolutions.
"""


from .body_of_the_last_response import BodyOfTheLastResponse

from .cookies import Cookies, CookiesOnTheAPISession

from .headers_of_the_last_response import HeadersOfTheLastResponse

from .status_code_of_the_last_response import StatusCodeOfTheLastResponse


# Natural-language-enabling syntactic sugar
TheBodyOfTheLastResponse = BodyOfTheLastResponse
TheCookies = Cookies
TheCookiesOnTheAPISession = CookiesOnTheAPISession
TheHeadersOfTheLastResponse = HeadersOfTheLastResponse
TheStatusCodeOfTheLastResponse = StatusCodeOfTheLastResponse


__all__ = [
    "BodyOfTheLastResponse",
    "Cookies",
    "CookiesOnTheAPISession",
    "HeadersOfTheLastResponse",
    "StatusCodeOfTheLastResponse",
    "TheBodyOfTheLastResponse",
    "TheCookies",
    "TheCookiesOnTheAPISession",
    "TheHeadersOfTheLastResponse",
    "TheStatusCodeOfTheLastResponse",
]
