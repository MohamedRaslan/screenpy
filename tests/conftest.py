from unittest import mock

import pytest

from screenpy.core import AnActor
from screenpy.web.selenium.abilities import AuthenticateWith2FA, BrowseTheWeb
from screenpy.api.abilities import MakeAPIRequests


@pytest.fixture(scope="function")
def Tester():
    """Provide an Actor with mocked web browsing abilities."""
    AuthenticateWith2FA_Mocked = mock.Mock(spec=AuthenticateWith2FA)
    AuthenticateWith2FA_Mocked.otp = mock.Mock()
    BrowseTheWeb_Mocked = mock.Mock(spec=BrowseTheWeb)
    BrowseTheWeb_Mocked.browser = mock.Mock()

    return AnActor.named("Tester").who_can(
        AuthenticateWith2FA_Mocked, BrowseTheWeb_Mocked
    )


@pytest.fixture(scope="function")
def APITester():
    """Provide an Actor with mocked API testing abilities."""
    MakeAPIRequests_Mocked = mock.Mock(spec=MakeAPIRequests)
    MakeAPIRequests_Mocked.session = mock.Mock()

    return AnActor.named("Tester").who_can(MakeAPIRequests_Mocked)
