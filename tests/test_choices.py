"""Test ``sopel_8ball.choices``."""
from __future__ import annotations

from sopel_8ball.choices import (AbstractChoiceProvider, Classic, Snarky,
                                 Spooky, Weeaball)


def test_abstract_provider():
    class MockChoice(AbstractChoiceProvider):
        def choices(self):
            return ('a',)

    provider = MockChoice()
    assert provider.query(None, None) == 'a'


def test_classic():
    provider = Classic()
    choices = provider.choices()

    assert len(choices) == 20
    assert provider.query(None, None) in choices


def test_snarky():
    provider = Snarky()
    choices = provider.choices()

    assert len(choices) == 20
    assert provider.query(None, None) in choices


def test_spooky():
    provider = Spooky()
    choices = provider.choices()

    assert len(choices) == 20
    assert provider.query(None, None) in choices


def test_weeaball():
    provider = Weeaball()
    choices = provider.choices()

    assert len(choices) == 23
    assert provider.query(None, None) in choices
