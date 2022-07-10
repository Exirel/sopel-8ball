"""Choices module for the magic 8 ball."""
from __future__ import generator_stop

import abc
import random
from typing import Tuple

from sopel.bot import Sopel  # type: ignore
from sopel.config import Config  # type: ignore
from sopel.tools import Identifier  # type: ignore


class AbstractChoiceProvider(abc.ABC):
    """Base provider class of 8 ball choices.

    A provider will be set up and then can be used to query the magic 8 ball
    from a destination (usually a channel) and a user::

        >>> magic8ball = MyChoiceProvider()
        >>> magic8ball.setup(bot)
        >>> magic8ball.query(channel, user)
        'This is my choice!'

    """
    def setup(self, bot: Sopel) -> None:
        """Set up the choices provider for this instance of Sopel.

        No-op by default.
        """

    def configure(self, settings: Config) -> None:
        """Configure the choices provider for this configuration.

        No-op by default.
        """

    @abc.abstractmethod
    def choices(self) -> Tuple[str, ...]:
        """Retrieve available choices from this magic 8 ball.

        :return: all possible choices for this 8 ball

        This is the list of choices unfiltered and valid for any destination
        and any user.
        """

    def query(self, destination: Identifier, user: Identifier) -> str:
        """Query the 8 ball for one of its choice.

        :param bot: sopel instance used to query the magic 8 ball
        :param trigger: trigger that triggered the query
        :return: the 8 ball's answer to that query
        """
        return random.choice(self.choices())


class Classic(AbstractChoiceProvider):
    """The classic magic 8 ball."""
    def choices(self) -> Tuple[str, ...]:
        return (
            # affirmative answers
            "It is Certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely.",
            "You may rely on it.",

            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",

            # non-committal answers
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.",
            "Cannot predict now.",
            "Concentrate and ask again.",

            # negative answers
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful.",
        )


class Snarky(AbstractChoiceProvider):
    """A snarky magic 8 ball."""
    def choices(self) -> Tuple[str, ...]:
        return (
            # affirmative answers
            "What’s the opposite of no?",
            "Is the sun hot?",
            "Heck yes!",
            "Of course, duh!",
            "Yeah, sure.",

            # non-committal answers
            "No comment.",
            "Cool query.",
            "I wasn’t born for this.",
            "Sorry, I wasn't listening.",
            "Please cancel my subscription to your issues.",

            # negative answers
            "What’s the opposite of yes?",
            "Is the sun cold?",
            "Hell to the no!",
            "You're joking, right?",
            "Ewwww...no!",

            "My answer is a resounding no!",
            "Frankly, my dear—no!",
            "No no no no no no no no no no no!",
            "Would you take \"no\" for an answer?",
            "Not in this lifetime!",
        )


class Spooky(AbstractChoiceProvider):
    """A spooky magic 8 ball."""
    def choices(self) -> Tuple[str, ...]:
        return (
            # affirmative answers
            "The ghost over your shoulder said yes.",
            "The accursed screams in agreement.",
            "The elders smile from the deep.",
            "I've seen this in the dreams of a Great Old One.",
            "For once, eerie voices whisper in harmony.",

            # non-committal answers
            "The abyss remains silent.",
            "I hear the whispers of a thousand voices, "
            "but none have your answer.",
            "The unfathomable truth cannot be revealed.",
            "In the darkness this won't matter anymore.",
            "From the depth comes no answer.",

            "The spirits are bored of this tune.",
            "The answer lies beyond the stars, ineffable.",
            "Answers are lost in the midst of black seas of infinity.",
            "You shall go mad from the revelation of the truth.",
            "I hear your call, yet their shrieking keeps me silent.",

            # negative answers
            "This would anger the old gods.",
            "This will bring sorrow and tears.",
            "The elders scowl from the deep.",
            "Hidden and fathomless minds pulsate in rage.",
            "The underworld grumbles with repudiation.",
        )
