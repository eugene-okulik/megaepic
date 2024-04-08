import requests
import pytest


@pytest.fixture(scope="session")
def before_run_and_end():
    print('Start testing')
    yield
    print('Testing complete')


@pytest.fixture()
def before_all_tests_end():
    print('before test')
    yield
    print('after test')


@pytest.fixture()
def get_object_id():
    body = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'content-type': 'application/json'}
    response = requests.post('https://api.restful-api.dev/objects', json=body, headers=headers)
    object_id = response.json()['id']
    yield object_id
    print('delete the post')
    requests.delete(f'https://api.restful-api.dev/objects/{object_id}')


@pytest.fixture()
def num():
    return 1
