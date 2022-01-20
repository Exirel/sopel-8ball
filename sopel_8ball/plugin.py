"""Magic 8 ball plugin"""
from __future__ import generator_stop

from sopel import plugin  # type: ignore
from sopel.bot import Sopel, SopelWrapper  # type: ignore
from sopel.config import Config  # type: ignore
from sopel.trigger import Trigger  # type: ignore

from sopel_8ball import config, managers


def setup(bot: Sopel) -> None:
    """Setup the manager."""
    bot.settings.define_section('magic8ball', config.Magic8ballSection)
    managers.manager.setup(bot)


def configure(settings: Config) -> None:
    """Configure the magic 8 ball plugin."""
    settings.define_section('magic8ball', config.Magic8ballSection)
    provider_list = ', '.join(managers.manager.provider_names)
    settings.magic8ball.configure_setting(
        'choices',
        'Pick a magic 8 ball choices type: {}: '.format(provider_list)
    )

    managers.manager.configure(settings)


@plugin.command('8ball', '8b')
@plugin.example('.8ball Do androids dream of electric sheep?', user_help=True)
def query(bot: SopelWrapper, trigger: Trigger) -> None:
    """Query the magic 8 ball for an answer."""
    reply = bot.reply
    if trigger.is_privmsg:
        reply = bot.say

    if not trigger.group(3):
        reply('What is your query?')
        return

    reply(managers.manager.provider.query(trigger.sender, trigger.nick))
