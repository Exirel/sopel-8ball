"""Magic 8 ball plugin"""
from __future__ import generator_stop

from sopel import plugin  # type: ignore
from sopel.bot import SopelWrapper  # type: ignore
from sopel.trigger import Trigger  # type: ignore

from sopel_8ball.managers import manager


def setup(bot):
    """Setup the manager."""
    manager.setup(bot)


@plugin.command('8ball')
def query(bot: SopelWrapper, trigger: Trigger):
    """Query the magic 8 ball for an answer."""
    if not trigger.group(3):
        bot.reply('')
        return

    manager.provider.query(trigger.sender, trigger.nick)
