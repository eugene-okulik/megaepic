import requests
import pytest
import allure


@pytest.fixture
def num():
    return 3


@allure.feature('Posts')
@allure.story('Manipulate posts')
@pytest.mark.medium
def test_delete(get_object_id):
    requests.delete(f'https://api.restful-api.dev/objects{get_object_id}').json()


@allure.feature('Example')
@allure.story('Some to fun')
def test_num(num):
    with allure.step('Equaling is correct'):
        assert num == 12
    print(num)
