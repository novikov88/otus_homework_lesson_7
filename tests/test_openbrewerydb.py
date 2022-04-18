"""
Проверка сервиса https://www.openbrewerydb.org/
Проверки включают в себя:
- Проверка статуса ответа
- Валидация схемы
- Проверка наличия городов
- Проверка нескольких пивоварен на наличие в вебсайте "http"
- Проверка кодировки
- Проверка заголовка
Дата: 14.04.2022
"""
import requests
import pytest
from jsonschema import validate

r = requests.get('https://api.openbrewerydb.org/breweries')


# status code check
def test_check_status_base_url():
    assert r.status_code == 200


# schema validation
def test_schema_check():
    schema = {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"},
            "brewery_type": {"type": "string"},
            "street": {"type": ["string", "null"]},
            "address_2": {"type": ["string", "null"]},
            "address_3": {"type": ["string", "null"]},
            "city": {"type": "string"},
            "state": {"type": "string"},
            "county_province": {"type": ["string", "null"]},
            "postal_code": {"type": "string"},
            "country": {"type": "string"},
            "longitude": {"type": ["string", "null"]},
            "latitude": {"type": ["string", "null"]},
            "phone": {"type": ["string", "null"]},
            "website_url": {"type": ["string", "null"]},
            "updated_at": {"type": "string"},
            "created_at": {"type": "string"}
        },

    }
    for value in range(len(r.json())):
        validate(instance=r.json()[value], schema=schema)


# city check
@pytest.mark.parametrize("test_input", ['Fayetteville', 'Windsor', 'Miami', 'Oregon City', 'Chardon'],
                         ids=['city of Fayetteville in text', 'city of Windsor in text', 'city of Miami in text',
                              'city of Oregon City in text', 'city of Chardon in text'])
def test_search_city(test_input):
    assert test_input in r.text


# web site check
@pytest.mark.parametrize("test_input", [1, 3, 5, 7, 11, 13, 15, 18, 19],
                         ids=['entry 1 has the value "http://" in the website',
                              'entry 3 has the value "http://" in the website',
                              'entry 5 has the value "http://" in the website',
                              'entry 6 has the value "http://" in the website',
                              'entry 11 has the value "http://" in the website',
                              'entry 13 has the value "http://" in the website',
                              'entry 15 has the value "http://" in the website',
                              'entry 18 has the value "http://" in the website',
                              'entry 19 has the value "http://" in the website'])
def test_check_http_website_url(test_input):
    website_url = r.json()[test_input]['website_url']
    assert 'http://' in website_url


# encoding check
def test_check_encoding():
    assert r.encoding == 'utf-8'


# headers check
def test_check_headers():
    assert r.headers['content-type'] == 'application/json; charset=utf-8'
