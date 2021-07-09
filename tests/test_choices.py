"""Test ``sopel_8ball.choices``."""
from __future__ import generator_stop

from sopel_8ball.choices import AbstractChoiceProvider, Classic, Snarky


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
