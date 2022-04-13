"""
Проверка сервиса https://www.openbrewerydb.org/
Проверки включают в себя:
- Проверка статуса ответа
- Проверка заголовка
- Проверка наличия городов
- Проверка нескольких пивоварен на наличие в вебсайте "http"
- Проверка кодировки

Дата: 14.04.2022
"""
import requests
import pytest

r = requests.get('https://jsonplaceholder.typicode.com/posts')


# status code check
def test_check_status_base_url():
    assert r.status_code == 200


# headers check
def test_check_headers():
    assert r.headers['content-type'] == 'application/json; charset=utf-8'


def test_check_id(fixture_with_params):
    r1 = requests.get('https://jsonplaceholder.typicode.com/posts/' + fixture_with_params)
    assert r1.json()['id'] == int(fixture_with_params)


# def test_check_id_not_more_100(fixture_with_params_100):
#     response = requests.get('https://jsonplaceholder.typicode.com/posts')
#     for value in range(fixture_with_params_100):
#         assert response.json()[value]['id'] <= fixture_with_params_100
#
#
# @pytest.mark.parametrize("test_input", ['ERROR', 'WARNING', 'WARN'])
# def test_check_errors_in_body(test_input, fixture_with_params):
#     resp = requests.get('https://jsonplaceholder.typicode.com/posts/' + fixture_with_params)
#     assert test_input not in resp.json()['body']
