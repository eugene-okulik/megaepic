import pytest
import requests


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
