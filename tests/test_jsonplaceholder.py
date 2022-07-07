"""
Проверка сервиса https://www.openbrewerydb.org/
Проверки включают в себя:
- Проверка статуса ответа
- Валидация схемы
- Проверка заголовка
- Проверка соответствия Id
- Проверка вывода результата не более 100 записей
- Проверка отсутствия ошибок ('ERROR', 'WARNING', 'WARN') в json
Дата: 14.04.2022
"""
import requests
import pytest
import json
from jsonschema import validate

r = requests.get('https://jsonplaceholder.typicode.com/posts')
d1 = r.json()
s1 = json.dumps(d1)


# status code check
def test_check_status_base_url():
    assert r.status_code == 200


# schema validation
def test_check_schema():
    schema = {
        "type": "object",
        "properties": {
            "userId": {"type": "number"},
            "id": {"type": 'number'},
            "title": {"type": "string"},
            "body": {"type": "string"}
        },
    }
    for value in range(len(r.json())):
        validate(instance=r.json()[value], schema=schema)


# headers check
def test_check_headers():
    assert r.headers['content-type'] == 'application/json; charset=utf-8'


# id check
def test_check_id(fixture_with_params):
    r1 = requests.get('https://jsonplaceholder.typicode.com/posts/' + fixture_with_params)
    assert r1.json()['id'] == int(fixture_with_params)


# check up to 100 results
def test_check_id_not_more_100(fixture_with_params_100):
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    for value in range(fixture_with_params_100):
        assert response.json()[value]['id'] <= fixture_with_params_100


# check for errors in json
@pytest.mark.parametrize("test_input", ['ERROR', 'WARNING', 'WARN'])
def test_check_errors_in_body(test_input, fixture_with_params):
    resp = requests.get('https://jsonplaceholder.typicode.com/posts/' + fixture_with_params)
    assert test_input not in resp.json()['body']
