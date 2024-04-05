import pytest
import requests
from pydantic import BaseModel, Field
from dataclasses import dataclass


class ObjectData(BaseModel):
    year: int
    price: float
    CPU_model: str = Field(alias='CPU model')
    Hard_disk_size: str = Field(alias='Hard disk size')


class Objects(BaseModel):
    id: str
    name: str
    data: ObjectData
    createdAt: str


class DeletedObject(BaseModel):
    message: str


@pytest.mark.medium
def test_get_one_post(get_object_id, before_run_and_end):
    print('test')
    response = requests.get(f'https://api.restful-api.dev/objects/{get_object_id}')
    assert response.json()['id'] == get_object_id


@pytest.mark.medium
def test_get_all_posts(before_all_tests_end):
    response = requests.get('https://api.restful-api.dev/objects').json()
    count_posts = len(response)
    assert len(response) == count_posts


@pytest.mark.critical
def test_patch_one_post(get_object_id, before_all_tests_end):
    body = {
        "name": "New name for test"
    }
    response = requests.patch(f'https://api.restful-api.dev/objects/{get_object_id}', json=body)
    assert response.json()['name'] == 'New name for test'


@pytest.mark.parametrize('name', ['name1', 'name2', 'name3'])
def test_add_post(before_all_tests_end, name):
    body = {
        "name": name,
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'content-type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    assert response.status_code == 200
    assert response.json()['name'] == name
    print(response.json()['name'])
    Objects(**response.json())


@pytest.mark.parametrize('color', ['blue', 'green', 'red'])
def test_put_post(get_object_id, before_all_tests_end, color):
    body = {
        "name": "Somename",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": color
        }
    }
    headers = {'content-type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{get_object_id}', json=body, headers=headers)
    assert response.json()['data']['color'] == color


def test_delete_posts(get_object_id, before_all_tests_end):
    response = requests.delete(f'https://api.restful-api.dev/objects/{get_object_id}').json()
    DeletedObject(**response)
