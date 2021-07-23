"""
Resolutions are expected results asserted by Actors, compared against the
answers to their Questions.

These form the second half of test assertions in Screenplay Pattern; the
first half is handled by Questions.
"""


from .is_clickable import IsClickable
from .is_visible import IsVisible


# Natural-language-enabling syntactic sugar
IsEnabled = Enabled = Clickable = IsClickable
IsDisplayed = Displayed = Visible = IsVisible


__all__ = [
    "Clickable",
    "Displayed",
    "Enabled",
    "IsClickable",
    "IsDisplayed",
    "IsEnabled",
    "IsVisible",
    "Visible",
]
