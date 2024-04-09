from megaepic.test_api_egamidov.endpoints.God_of_endpoints import Endpoint
import requests
import allure


class UpdateObject(Endpoint):

    @allure.step("Updating post_object")
    def make_changes_in_post(self, test_object_id, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.put(f'{self.url}/{test_object_id}', json=body, headers=headers)
        self.json = self.response.json()
        return self.response
