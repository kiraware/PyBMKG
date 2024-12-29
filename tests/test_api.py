import pytest
from aiohttp import ClientSession
from bmkg.api import API


def test_api_without_base_url():
    with pytest.raises(NotImplementedError):
        API()


def test_api_with_base_url():
    class TestAPI(API):
        base_url = "http://example.com"

    api = TestAPI(session=ClientSession())

    assert api.base_url == "http://example.com"
