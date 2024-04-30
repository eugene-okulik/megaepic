from endpoints.God_of_endpoints import Endpoint
import requests
import allure


class DeleteObject(Endpoint):

    @allure.step('Delete the object')
    def delete_object(self, test_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.delete(f'{self.url}/{test_object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
