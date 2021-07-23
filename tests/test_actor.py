from unittest import mock

import pytest

from screenpy.core import Actor
from screenpy.core.exceptions import UnableToPerform


def test_can_be_instantiated():
    a1 = Actor.named("test")
    a2 = Actor.named("test").can(None)
    a3 = Actor.named("test").who_can(None)
    a4 = Actor.named("test").who_can(None).with_cleanup_task(None)

    assert isinstance(a1, Actor)
    assert isinstance(a2, Actor)
    assert isinstance(a3, Actor)
    assert isinstance(a4, Actor)


def test_complains_for_missing_abilities():
    actor = Actor.named("Tester")

    with pytest.raises(UnableToPerform):
        actor.ability_to(1)


def test_find_abilities():
    ability = 1
    actor = Actor.named("test").who_can(ability)

    assert actor.ability_to(int) is ability


def test_performs_cleanup_tasks_when_exiting():
    mocked_task = mock.Mock()
    actor = Actor.named("test").with_cleanup_task(mocked_task)

    actor.exit()

    mocked_task.perform_as.assert_called_once_with(actor)
    assert len(actor.cleanup_tasks) == 0


def test_forgets_abilities_when_exiting():
    mocked_ability = mock.Mock()
    actor = Actor.named("test").who_can(mocked_ability)

    actor.exit()

    mocked_ability.forget.assert_called_once()
    assert len(actor.abilities) == 0
