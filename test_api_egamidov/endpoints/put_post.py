from endpoints.God_of_endpoints import Endpoint
import requests
import allure


class PutObject(Endpoint):

    @allure.step('Put new object')
    def put_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(
            self.url,
            json=body,
            headers=headers)
        self.json = self.response.json()
        return self.response
