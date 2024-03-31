import requests


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
    print(response)
    post_id = response['id']
    return post_id


post_id = create()


def update_put(post_id):
    body = {
        "name": "Apple MacBook Pro 13226",
        "data": {
            "year": 2019,
            "price": 2049.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB",
            "color": "silver"
        }
}
    headers = {'Content-Type': 'application/json'}
    response = requests.put(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    print(response)


def update_patch(post_id):
    body = {
        "name": "IZI MACK (Updated Name)"
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.patch(f'https://api.restful-api.dev/objects/{post_id}', json=body, headers=headers).json()
    print(response)


def getting_get():
    response = requests.get('https://api.restful-api.dev/objects').json()
    print(response)


def delete_del(post_id):
    response = requests.delete(f'https://api.restful-api.dev/objects/{post_id}').json()
    print(response)


update_patch(post_id)
update_put(post_id)
delete_del(post_id)
