import pytest
import requests


@pytest.fixture(params=['1', '2', '3', '4'])
def fixture_with_params(request):
    return request.param


@pytest.fixture(params=[100])
def fixture_with_params_100(request):
    return request.param


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://ya.ru",
        help="This is request url"
    )

    parser.addoption(
        "--status_code",
        action="store",
        default='200',
        choices=['200', '404', '401', '500'],
        help="This is status code"
    )

    parser.addoption(
        "--method",
        default='get',
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def base_status_code(request):
    return request.config.getoption("--status_code")


@pytest.fixture
def request_method(request):
    return getattr(requests, request.config.getoption("--method"))
