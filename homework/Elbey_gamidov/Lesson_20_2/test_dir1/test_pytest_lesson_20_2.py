import allure
import requests
import pytest


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение объекта по айди')
@pytest.mark.medium
def test_get_one_post(get_object_id, before_run_and_end):
    print('test')
    with allure.step(f'Run get request for post with id = {get_object_id}'):
        response = requests.get(f'https://api.restful-api.dev/objects/{get_object_id}')
    with allure.step(f'Check that post id is {get_object_id}'):
        assert response.json()['id'] == get_object_id


@allure.feature('Posts')
@allure.story('Get posts')
@allure.title('Получение всех созданных объектов')
@pytest.mark.medium
def test_get_all_posts(before_all_tests_end):
    response = requests.get('https://api.restful-api.dev/objects').json()
    with allure.step(f'Count of all objects = {len(response)}'):
        count_posts = len(response)
        assert len(response) == count_posts


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Обновляем имя объекта, который уже есть в системе')
@pytest.mark.critical
def test_patch_one_post(get_object_id, before_all_tests_end):
    body = {
        "name": "New name for test"
    }
    response = requests.patch(
        f'https://api.restful-api.dev/objects/{get_object_id}', json=body)
    with allure.step('Check this name = New name for test'):
        assert response.json()['name'] == 'New name for test'


@allure.feature('Posts')
@allure.story('Create posts')
@allure.title('Создание объекта')
@pytest.mark.parametrize('name', ['name1', 'name2', 'name3'])
def test_add_post(before_all_tests_end, name):
    with allure.step('Prepate test data'):
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
    with allure.step('Run request to create an object'):
        response = requests.post(
            'https://api.restful-api.dev/objects', json=body, headers=headers)
    with allure.step('Check response code is 200'):
        assert response.status_code == 200
    with allure.step('Check response name is correct'):
        assert response.json()['name'] == name


@allure.feature('Posts')
@allure.story('Manipulate posts')
@allure.title('Удаление объекта')
@pytest.mark.medium
def test_delete(get_object_id):
    requests.delete(f'https://api.restful-api.dev/objects{get_object_id}').json()
