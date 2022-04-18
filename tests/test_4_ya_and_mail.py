"""
Тест проверяет дефолтный url(https://ya.ru) и стандартный код ответа 200
для запуска с параметрами использовать "--url=https://yandex.ru/fwe --status_code=404" или
--url=https://otus.ru --status_code=200
"""


def test_api_filtering(base_url, base_status_code, request_method):
    response = request_method(url=base_url)
    assert str(response.status_code) == base_status_code
