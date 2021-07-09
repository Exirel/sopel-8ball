"""Integration test for the 8ball plugin."""
from __future__ import generator_stop

import re

import pytest
from sopel.tests import rawlist

from sopel_8ball import choices, managers


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
    with pytest.raises(RuntimeError):
        # since the plugin is not set up, the manager's provider isn't set
        managers.manager.provider

    botfactory.preloaded(tmpconfig, preloads=['8ball'])
    assert isinstance(managers.manager.provider, choices.Classic)


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
