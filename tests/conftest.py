import pytest
import requests


@pytest.fixture(params=['1', '2', '3', '4'])
def fixture_with_params(request):
    return request.param


# @pytest.fixture(params=[100])
# def fixture_with_params_100(request):
#     return request.param
#
#
# class APIClient:
#     def __init__(self, base_address):
#         self.base_address = base_address
#
#     def get(self):
#         return requests.get(url=self.base_address)
#
#
# def pytest_addoption(parser):
#     parser.addoption(
#         "--url",
#         action="store",
#         default="https://ya.ru",
#         help="This is request url"
#     )
#
#
# @pytest.fixture(scope="session")
# def api_client(request):
#     base_url = request.config.getoption("--url")
#     return APIClient(base_address=base_url)
