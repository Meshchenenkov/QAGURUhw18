import json
import requests
from jsonschema import validate
from schemas import post_create, post_register_unsuccessful, get_single_user_not_found


url1 = "https://reqres.in"
key = {'x-api-key': 'reqres-free-v1'}
#1. а ручки-то вот они на каждый из методов GET/POST/PUT/DELETE ручек reqres.in
#2. Позитивные/Негативные тесты на одну из ручек.
#3. На разные статус-коды 200/201/204/404/400
#4. На разные схемы (4-5 схем)
def test_update_200status_put_positive():
    response = requests.request("PUT", url=f"{url1}/api/users/2", headers=key, params={"name": "morpheus", "job": "zion resident"})
    assert response.status_code == 200
    with open("put_update.json") as file:
        validate(response.json(), schema=json.loads(file.read()))


def test_register_unsuccessful_400status_post_negative():
    response = requests.post(url=f'{url1}/api/login', headers=key, json={"email": "peter@klaven"})
    assert response.status_code == 400
    validate(response.json(), schema=post_register_unsuccessful)


def test_single_user_not_found_404status_get_negative():
    response = requests.get(url="https://reqres.in/api/users/23", headers=key)
    assert response.status_code == 404
    validate(response.json(), schema=get_single_user_not_found)


def test_get_users_delay_large_response_not_200():
    response = requests.get(url=f"{url1}/api/users", params={"delay": 30}, headers=key)
    assert response.status_code != 200
    getting_status_code = response.status_code
    print(getting_status_code)
    assert getting_status_code == 503


#5 ...без ответа
def test_get_users_204status_delete_positive_emptyresponse():
    response = requests.delete(url=f'{url1}/api/users/2', headers=key)
    assert response.status_code == 204
    response is None


#6. На бизнес-логику (заметить какую-то фичу и автоматизировать, как делали на уроке)
def test_create_201status_post_positive_created_name_and_job_equal_request():
    payload = {"name": "morpheus2", "job": "leader2"}
    response = requests.request("POST", url=f'{url1}/api/users', headers=key, data=payload)
    assert response.status_code == 201
    body = response.json()
    validate(body, schema=post_create)
    assert payload["name"] == body["name"]
    assert payload["job"] == body["job"]


def test_get_resource_returns_unique_resource():
    response = requests.get(url=f"{url1}/api/unknown", params={"page": 3, "per_page": 2}, headers=key)
    ids = [element["id"] for element in response.json()["data"]]
    assert len(ids) == len(set(ids))



