from megaepic.test_api_egamidov.endpoints.God_of_endpoints import Endpoint
import requests
import allure


class PatchObject(Endpoint):

    @allure.step('Patch new object')
    def patch_new_object(self, body, headers=None):
        headers = headers if headers else self.headers
        self.response = requests.patch(
            self.url,
            json=body,
            headers=headers)
        self.json = self.response.json()
        return self.response
