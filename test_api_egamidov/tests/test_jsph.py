from megaepic.test_api_egamidov.endpoints.create_object import CreateObject


def test_add_post(create_post_endpoint):
    payload = {
        "name": "somename",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    headers = {'content-type': 'application/json'}
    create_post_endpoint.create_new_object(payload=payload, headers=headers)
    assert create_post_endpoint.create_new_object(payload, headers).status_code == 200
    create_post_endpoint.check_response_name_is_correct(payload['name'])
