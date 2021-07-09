"""Configuration for the magic 8 ball plugin."""
from sopel import config  # type: ignore

from sopel_8ball.managers import manager


class Magic8ballSection(config.types.StaticSection):
    """Configuration section for this plugin."""
    choices = config.types.ChoiceAttribute('choices',
                                           manager.provider_names,
                                           default='classic')
    """Which type of magic 8 ball choices to use."""
