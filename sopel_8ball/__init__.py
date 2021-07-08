"""Sopel Magic 8 ball plugin."""
from __future__ import generator_stop

import pkg_resources  # type: ignore

__version__ = pkg_resources.get_distribution('sopel-8ball').version
