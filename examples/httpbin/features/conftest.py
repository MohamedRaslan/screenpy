"""
Fixtures for API testing.
"""

from typing import Generator

import pytest

from screenpy.core import AnActor
from screenpy.api.abilities import MakeAPIRequests


@pytest.fixture
def Perry() -> Generator:
    """An Actor who can make API requests."""
    the_actor = AnActor.named("Perry").who_can(MakeAPIRequests())
    yield the_actor
    the_actor.exit_stage_left()
