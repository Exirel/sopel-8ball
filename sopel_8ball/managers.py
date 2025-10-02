"""Manager for magic 8 Ball"""
from __future__ import annotations

from typing import Optional, Tuple

# TODO: use stdlib importlib.metadata when possible, after dropping py3.9.
# Stdlib does not support `entry_points(group='filter')` until py3.10, but
# fallback logic is more trouble than it's worth when e.g. clean Ubuntu
# py3.10 envs include old versions of this backport.
import importlib_metadata
from sopel.bot import Sopel  # type: ignore
from sopel.config import Config  # type: ignore

from .choices import AbstractChoiceProvider

PROVIDERS_ENTRY_POINT = 'sopel_8ball.choices'


class Manager:
    """Manage magic 8 ball providers."""
    def __init__(self) -> None:
        self._provider: Optional[AbstractChoiceProvider] = None
        self._provider_list: Optional[Tuple[str, ...]] = None

    @property
    def provider(self):
        """Magic 8 ball provider."""
        if self._provider is None:
            raise RuntimeError('Magic 8 ball provider is not configured yet.')
        return self._provider

    @property
    def provider_names(self) -> Tuple[str, ...]:
        """Names of the available providers."""
        if self._provider_list is None:
            entry_points = importlib_metadata.entry_points(
                group=PROVIDERS_ENTRY_POINT,
            )
            self._provider_list = tuple(
                entry_point.name
                for entry_point in entry_points
            )
        return self._provider_list

    def load_provider(self, name: str) -> AbstractChoiceProvider:
        """Load provider from a name.

        :param name: name of the provider
        :return: a provider instance

        The provider will be loaded from an entry point and then instanciated
        to be returned as is (no setup, no configure).
        """
        entry_points = (e for e in importlib_metadata.entry_points(
            group=PROVIDERS_ENTRY_POINT, name=name,
        ))

        try:
            entry_point = next(entry_points)
        except StopIteration as err:
            raise RuntimeError('Cannot found 8ball choices %s' % name) from err

        # 3. load the entry point
        provider_maker = entry_point.load()
        provider = provider_maker()

        assert isinstance(provider, AbstractChoiceProvider)

        return provider

    def setup(self, bot: Sopel) -> None:
        """Set up the manager"""
        self._provider = self.load_provider(bot.settings.magic8ball.choices)
        self._provider.setup(bot)

    def configure(self, settings: Config) -> None:
        """Configure the magic 8 ball choices provider."""
        provider = self.load_provider(settings.magic8ball.choices)
        provider.configure(settings)


manager = Manager()
