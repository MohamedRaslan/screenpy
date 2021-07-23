"""
Questions are asked by Actors to determine the actual value from the
current state of the application under test.

These form the first half of test assertions in Screenplay Pattern; the
second half is handled by Resolutions.
"""


from .attribute import Attribute
from .browser_title import BrowserTitle
from .browser_url import BrowserURL
from .cookies import Cookies, CookiesOnTheWebSession
from .element import Element
from .list import List
from .number import Number
from .selected import Selected
from .text import Text
from .text_of_the_alert import TextOfTheAlert

# Natural-language-enabling syntactic sugar
TheAttribute = Attribute
TheBrowserTitle = BrowserTitle
TheBrowserURL = BrowserURL
TheCookies = Cookies
TheCookiesOnTheWebSession = CookiesOnTheWebSession
TheElement = Element
TheList = List
TheNumber = Number
TheSelected = Selected
TheText = Text
TheTextOfTheAlert = TextOfTheAlert


__all__ = [
    "Attribute",
    "BrowserTitle",
    "BrowserURL",
    "Cookies",
    "CookiesOnTheWebSession",
    "Element",
    "List",
    "Number",
    "Selected",
    "Text",
    "TextOfTheAlert",
    "TheAttribute",
    "TheBrowserTitle",
    "TheBrowserURL",
    "TheCookies",
    "TheCookiesOnTheWebSession",
    "TheElement",
    "TheList",
    "TheNumber",
    "TheSelected",
    "TheText",
    "TheTextOfTheAlert",
]
