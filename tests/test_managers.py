"""Test ``sopel_8ball.managers``."""
import pytest

from sopel_8ball import choices, managers


def test_manager_provider_names():
    assert managers.manager.provider_names == ('classic',)


def test_manager_load_provider():
    assert 'classic' in managers.manager.provider_names, (
        'Cannot test load if classic provider does not exist.')
    assert 'mockinvalid' not in managers.manager.provider_names, (
        'Cannot test load if "mockinvalid" provider exists. (Who created it?)')

    provider = managers.manager.load_provider('classic')
    assert isinstance(provider, choices.Classic)

    with pytest.raises(RuntimeError):
        managers.manager.load_provider('mockinvalid')
