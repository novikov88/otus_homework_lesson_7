"""
Проверка сервиса https://dog.ceo/dog-api/
Проверки включают в себя:
- Проверка статуса ответа
- Проверка наличия пород в целом
- Проверка разновидности породы спаниель до подвида
- Проверка статуса случайного изображения
- Проверка работоспособности показа нескольких случайных изображений (1, 25, 50)
Дата: 14.04.2022
"""
import pytest
import requests

r1 = requests.get('https://dog.ceo/api/breeds/list/all')
r2 = requests.get('https://dog.ceo/api/breed/hound/images/random')


# status code check
def test_check_status():
    assert r1.status_code == 200


# breed check
@pytest.mark.parametrize("test_input", ['african', 'mastiff', 'rottweiler', 'husky'],
                         ids=['breed african in text', 'breed mastiff in text', 'breed rottweiler in text',
                              'breed husky in text'])
def test_check_breeds(test_input):
    assert test_input in r1.text


# spaniel subspecies check
@pytest.mark.parametrize("test_input", ['blenheim', 'brittany', 'cocker', 'irish', 'japanese', 'sussex', 'welsh'],
                         ids=['spaniel blenheim in json', 'spaniel brittany in json', 'spaniel cocker in json',
                              'spaniel irish in json', 'spaniel japanese in json', 'spaniel sussex in json',
                              'spaniel welsh in json'])
def test_check_sub_breeds(test_input):
    assert test_input in r1.json()['message']['spaniel']


# check response status from random image
def test_check_status_json():
    assert r2.json()['status'] == "success"


# check multiple random images
@pytest.mark.parametrize("test_input", ['1', '25', '50'],
                         ids=['one random image', 'twenty five random image', 'fifty random images'])
def test_check_count_images(test_input):
    r3 = requests.get('https://dog.ceo/api/breeds/image/random/' + test_input)
    assert len(r3.json()['message']) == int(test_input)
