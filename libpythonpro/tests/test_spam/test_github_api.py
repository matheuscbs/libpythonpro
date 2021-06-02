from unittest.mock import Mock

import pytest as pytest

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars3.githubusercontent.com/u/68289167?v=4'
    resp_mock.json.return_value = {
        'login': 'matheus', 'id': 68289167,
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('matheus')
    assert avatar_url == url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('matheuscbs')
    assert 'https://avatars.githubusercontent.com/u/68289167?v=4' == url
