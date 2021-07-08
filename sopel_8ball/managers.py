"""Manager for magic 8 Ball"""
from __future__ import generator_stop

from typing import NoReturn, Optional

from sopel.bot import Sopel  # type: ignore

from .choices import AbstractChoiceProvider, Classic


class Manager:
    """Manage magic 8 ball providers."""
    @property
    def provider(self):
        """Magic 8 ball provider."""
        if self._provider is None:
            raise RuntimeError('Magic 8 ball provider is not configured yet.')
        return self._provider

    def __init__(self) -> None:
        self._provider: Optional[AbstractChoiceProvider] = None

    def setup(self, bot: Sopel) -> NoReturn:
        """Set up the manager"""
        self._provider = Classic()
        self._provider.setup(bot)


manager = Manager()
