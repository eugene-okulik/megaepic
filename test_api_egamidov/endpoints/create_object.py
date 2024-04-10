from endpoints.God_of_endpoints import Endpoint
import requests
import allure


class CreateObject(Endpoint):

    @allure.step('Create new object')
    def create_new_object(self, body, headers=None):
        if len(body['body']) > 1000:
            self.url = (f'{self.url}dlinnopost')
        headers = headers if headers else self.headers
        self.response = requests.post(
            self.url,
            json=body,
            headers=headers)
        self.json = self.response.json()
        return self.response
