import pytest

TEST_DATA = [
    {"name": "some_name",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1TB"}},
    {"name": "some_name1",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": "some_name2",
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
]


NEGATIVE_DATA = [
    {"name": ["some_name"],
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1TB"}},
    {"name": {"some_name1"},
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}},
    {"name": 123,
     "data": {"year": 2019, "price": 1849.99, "CPU model": "Intel Core i9", "Hard disk size": "1 TB"}}
]


@pytest.mark.parametrize('data', TEST_DATA)
def test_add_post(create_post_endpoint, data):
    create_post_endpoint.create_new_object(body=data)
    create_post_endpoint.check_response_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])


@pytest.mark.parametrize('data', NEGATIVE_DATA)
def test_negative_post(create_post_endpoint, data):
    create_post_endpoint.create_new_object(data)
    create_post_endpoint.check_response_is_200()
    create_post_endpoint.check_response_name_is_correct(data['name'])


@pytest.mark.parametrize('data', TEST_DATA)
def test_put_post(update_post_object_endpoint):
    update_post_object_endpoint.make_cnahges_in_post(id, TEST_DATA)
    update_post_object_endpoint.check_response_is_200()
    update_post_object_endpoint.check_response_name_is_correct(TEST_DATA['name'])


def test_patch_post(patch_post_endpoint):
    body = {
        "name": "Some_name_228",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "blue"
        }
    }
    patch_post_endpoint.patch_new_object(id, body)
    patch_post_endpoint.check_response_is_200()
    patch_post_endpoint.check_response_name_is_correct(body['name'])


def test_delete_post(delete_post_endpoint):
    delete_post_endpoint.delete_object(id)
    delete_post_endpoint.check_response_is_200()
