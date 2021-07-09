"""Magic 8 ball plugin"""
from __future__ import generator_stop

from sopel import plugin  # type: ignore
from sopel.bot import Sopel, SopelWrapper  # type: ignore
from sopel.trigger import Trigger  # type: ignore

from sopel_8ball.managers import manager


def setup(bot: Sopel):
    """Setup the manager."""
    manager.setup(bot)


@plugin.command('8ball')
def query(bot: SopelWrapper, trigger: Trigger) -> None:
    """Query the magic 8 ball for an answer."""
    reply = bot.reply
    if trigger.is_privmsg:
        reply = bot.say

    if not trigger.group(3):
        reply('What is your query?')
        return

    reply(manager.provider.query(trigger.sender, trigger.nick))
