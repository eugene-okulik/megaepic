import pytest
import requests


@pytest.fixture(scope="module")
def start_testing():
    print('Start testing')
    yield
    print('Testing completed')


@pytest.fixture()
def setup():
    print('before test')
    post_id = create()
    yield post_id
    delete_object(post_id)
    print('after test')


def create():
    body = {
        "name": "Apple MacBook Pro 162",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers).json()
    post_id = response['id']
    return post_id


def update_object_name(post_id, new_name):
    body = {
        "name": new_name
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    return response['name']


def get_object_by_id(post_id):
    response = requests.get(f'https://api.restful-api.dev/objects/{post_id}').json()
    return response


def delete_object(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}').json()
    return response


@pytest.mark.critical
@pytest.mark.parametrize('name', ['name1', 'name2', 'name3'])
def test_create_object(start_testing, setup, name):
    assert create_object(name) is not None


def create_object(name):
    body = {
        "name": name,
        "data": {
            "year": 2022,
            "price": 999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers).json()

    return response


@pytest.mark.medium
def test_update_object_name(setup):
    assert update_object_name(setup, 'name') == 'name'


@pytest.mark.medium
def test_get_object_by_id(setup):
    assert get_object_by_id(setup) is not None


@pytest.mark.medium
def test_delete_object(setup):
    response = delete_object(setup)
    assert response['message'] == f"Object with id = {setup} has been deleted."
