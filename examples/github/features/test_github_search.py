"""
An example of a test module that follows the typical pytest test
structure. These tests show off how to use custom tasks and Questions,
though they are a little bit contrived.
"""

from typing import Generator

import pytest
from selenium.webdriver import Firefox

from screenpy.core import Actor, given, then, when
from screenpy.core.actions import See
from screenpy.web.selenium.abilities import BrowseTheWeb
from screenpy.web.selenium.actions import Open
from screenpy.core.pacing import act, scene
from screenpy.core.resolutions import (
    ContainsTheText,
    ContainTheText,
    DoesNot,
    IsEqualTo,
    ReadsExactly,
)

from ..questions.number_of_search_results import NumberOfSearchResults
from ..questions.search_results_message import SearchResultsMessage
from ..tasks.search_github import SearchGitHub
from ..user_interface.github_home_page import URL


@pytest.fixture(scope="function", name="Perry")
def fixture_actor() -> Generator:
    """Create the Actor for our example tests!"""
    the_actor = Actor.named("Perry").who_can(BrowseTheWeb.using(Firefox()))
    yield the_actor
    the_actor.exit_stage_left()


@act("Search")
@scene("Search for the ScreenPy repository on GitHub")
def test_search_for_screenpy(Perry: Actor) -> None:
    """GitHub search finds the screenpy repository."""
    given(Perry).was_able_to(Open.their_browser_on(URL))
    when(Perry).attempts_to(SearchGitHub.for_text("perrygoy/screenpy"))
    then(Perry).should(
        See.the(SearchResultsMessage(), DoesNot(ContainTheText("couldn’t"))),
        See.the(SearchResultsMessage(), ReadsExactly("1 repository result")),
        See.the(NumberOfSearchResults(), IsEqualTo(1)),
    )


@act("Search")
@scene("Search for a nonexistant repository on GitHub")
def test_search_for_nonexistent_repo(Perry: Actor) -> None:
    """GitHub search fails to find a nonexistant repository."""
    nonexistant_repository = "perrygoy/i-never-made-this-repo"

    given(Perry).was_able_to(Open.their_browser_on(URL))
    when(Perry).attempts_to(SearchGitHub.for_text(nonexistant_repository))
    then(Perry).should(
        See.the(SearchResultsMessage(), ContainsTheText("We couldn’t find any")),
        See.the(SearchResultsMessage(), ContainsTheText(nonexistant_repository)),
        See.the(NumberOfSearchResults(), IsEqualTo(0)),
    )
