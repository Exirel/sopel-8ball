"""Test ``sopel_8ball.managers``."""
import pytest

from sopel_8ball import choices, config, managers


def test_manager_provider_names():
    assert managers.manager.provider_names == (
        'classic',
        'snarky',
        "spooky",
    )


def test_manager_load_provider():
    assert 'classic' in managers.manager.provider_names, (
        'Cannot test load if classic provider does not exist.')
    assert 'mockinvalid' not in managers.manager.provider_names, (
        'Cannot test load if "mockinvalid" provider exists. (Who created it?)')

    provider = managers.manager.load_provider('classic')
    assert isinstance(provider, choices.Classic)

    with pytest.raises(RuntimeError):
        managers.manager.load_provider('mockinvalid')


TMP_CONFIG = """
[core]
owner = testnick
nick = TestBot
enable = coretasks, 8ball
"""


def test_manager_setup_default(configfactory, botfactory):
    manager = managers.Manager()

    with pytest.raises(RuntimeError):
        # since the plugin is not set up, the manager's provider isn't set
        manager.provider

    tmpconfig = configfactory('test.cfg', TMP_CONFIG)
    mockbot = botfactory(tmpconfig)

    tmpconfig.define_section('magic8ball', config.Magic8ballSection)
    manager.setup(mockbot)

    assert isinstance(manager.provider, choices.Classic)


TMP_CONFIG_SNARKY = """
[core]
owner = testnick
nick = TestBot
enable = coretasks, 8ball

[magic8ball]
choices = snarky
"""


def test_manager_setup_snarky(configfactory, botfactory):
    manager = managers.Manager()
    tmpconfig = configfactory('test.cfg', TMP_CONFIG_SNARKY)
    mockbot = botfactory(tmpconfig)

    tmpconfig.define_section('magic8ball', config.Magic8ballSection)
    manager.setup(mockbot)

    assert isinstance(manager.provider, choices.Snarky)


TMP_CONFIG_SPOOKY = """
[core]
owner = testnick
nick = TestBot
enable = coretasks, 8ball

[magic8ball]
choices = spooky
"""


def test_manager_setup_spooky(configfactory, botfactory):
    manager = managers.Manager()
    tmpconfig = configfactory('test.cfg', TMP_CONFIG_SPOOKY)
    mockbot = botfactory(tmpconfig)

    tmpconfig.define_section('magic8ball', config.Magic8ballSection)
    manager.setup(mockbot)

    assert isinstance(manager.provider, choices.Spooky)
