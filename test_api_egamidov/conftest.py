import pytest
from endpoints.create_object import CreateObject
from endpoints.update_post import UpdateObject
from endpoints.patch_post import PatchObject
from endpoints.delete_object import DeleteObject


@pytest.fixture()
def update_post_object_endpoint():
    return UpdateObject()


@pytest.fixture
def create_post_endpoint():
    return CreateObject()


@pytest.fixture()
def patch_post_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_post_endpoint():
    return DeleteObject()


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
def test_object_id(create_post_endpoint):
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
    response = create_post_endpoint.create_new_object(body, headers)
    object_id = response.json()['id']
    return object_id


@pytest.fixture()
def num():
    return 1
