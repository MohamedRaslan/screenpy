from typing import Callable, Generator, Any
from unittest import mock

import pytest

from screenpy import AnActor, pacing, settings
from screenpy.abilities import AuthenticateWith2FA, BrowseTheWeb, MakeAPIRequests
from screenpy.narration.narrator import Narrator


@pytest.fixture(scope="function")
def Tester() -> AnActor:
    """Provide an Actor with mocked web browsing abilities."""
    AuthenticateWith2FA_Mocked = mock.Mock(spec=AuthenticateWith2FA)
    AuthenticateWith2FA_Mocked.otp = mock.Mock()
    BrowseTheWeb_Mocked = mock.Mock(spec=BrowseTheWeb)
    BrowseTheWeb_Mocked.browser = mock.Mock()

    return AnActor.named("Tester").who_can(
        AuthenticateWith2FA_Mocked, BrowseTheWeb_Mocked
    )


@pytest.fixture(scope="function")
def APITester() -> AnActor:
    """Provide an Actor with mocked API testing abilities."""
    MakeAPIRequests_Mocked = mock.Mock(spec=MakeAPIRequests)
    MakeAPIRequests_Mocked.session = mock.Mock()

    return AnActor.named("Tester").who_can(MakeAPIRequests_Mocked)


@pytest.fixture(scope="function")
def mocked_narrator() -> Generator[mock.MagicMock, Any, None]:
    """Mock out the Narrator for a test, replacing the old one afterwards."""
    MockNarrator = mock.MagicMock(spec=Narrator)
    old_narrator = pacing.the_narrator
    pacing.the_narrator = MockNarrator

    yield MockNarrator

    pacing.the_narrator = old_narrator


def mock_settings(**new_settings) -> Callable:
    """Mock one or more settings for the duration of a test."""
    def decorator(func: Callable) -> Callable:
        def wrapper(*args, **kwargs) -> Callable:
            old_settings = {
                key: getattr(settings, key)
                for key in new_settings.keys()
            }
            for key, value in new_settings.items():
                setattr(settings, key, value)

            try:
                func(*args, **kwargs)
            finally:
                for key, value in old_settings.items():
                    setattr(settings, key, value)

        return wrapper

    return decorator
