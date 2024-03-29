"""Integration test for the 8ball plugin."""
from __future__ import generator_stop

import re
from unittest import mock

import pytest
from sopel.tests import rawlist

from sopel_8ball import choices, managers
from sopel_8ball.plugin import configure


TMP_CONFIG = """
[core]
owner = testnick
nick = TestBot
enable = coretasks, 8ball
"""


@pytest.fixture
def tmpconfig(configfactory):
    return configfactory('test.cfg', TMP_CONFIG)


@pytest.fixture
def mockbot(tmpconfig, botfactory):
    return botfactory.preloaded(tmpconfig, preloads=['8ball'])


@pytest.fixture
def irc(mockbot, ircfactory):
    server = ircfactory(mockbot)
    server.bot.backend.clear_message_sent()
    return server


def test_8ball_default_provider(tmpconfig, botfactory):
    botfactory.preloaded(tmpconfig, preloads=['8ball'])
    assert isinstance(managers.manager.provider, choices.Classic)


def test_8ball_commands(mockbot):
    assert mockbot.rules.has_command('8ball', follow_alias=False)
    assert not mockbot.rules.has_command('8b', follow_alias=False)
    assert not mockbot.rules.has_command('8', follow_alias=False)
    assert mockbot.rules.has_command('8b', follow_alias=True)
    assert mockbot.rules.has_command('8', follow_alias=True)


def test_8ball_channel(irc, userfactory):
    user = userfactory('Exirel')
    irc.say(user, '#channel', '.8ball this is my query')
    assert len(irc.bot.backend.message_sent) == 1

    reply = irc.bot.backend.message_sent[0]
    pattern = rawlist("PRIVMSG #channel :Exirel: .+")[0]

    assert re.match(pattern, reply)


def test_8ball_pm(irc, userfactory):
    user = userfactory('Exirel')
    irc.pm(user, '.8ball this is my query')
    assert len(irc.bot.backend.message_sent) == 1

    reply = irc.bot.backend.message_sent[0]
    pattern = rawlist("PRIVMSG Exirel :.+")[0]

    assert re.match(pattern, reply)


def test_8ball_channel_no_query(irc, userfactory):
    user = userfactory('Exirel')
    irc.say(user, '#channel', '.8ball')
    assert len(irc.bot.backend.message_sent) == 1

    assert irc.bot.backend.message_sent == rawlist(
        'PRIVMSG #channel :Exirel: What is your query?',
    )


def test_8ball_pm_no_query(irc, userfactory):
    user = userfactory('Exirel')
    irc.pm(user, '.8ball')
    assert len(irc.bot.backend.message_sent) == 1

    assert irc.bot.backend.message_sent == rawlist(
        'PRIVMSG Exirel :What is your query?',
    )


def test_configure(tmpconfig):
    with mock.patch('sopel.config.types.get_input') as mock_input:
        mock_input.side_effect = ["classic"]
        configure(tmpconfig)

    assert 'magic8ball' in tmpconfig
    assert hasattr(tmpconfig.magic8ball, 'choices')

    assert tmpconfig.magic8ball.choices == 'classic'
