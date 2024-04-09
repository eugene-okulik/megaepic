import allure


class Endpoint:
    url = 'https://api.restful-api.dev/objects'
    headers = {'content-type': 'application/json'}
    response = None
    json = None


    @allure.step('Check response name')
    def check_response_name_is_correct(self, name):
        assert self.response.json()['name'] == name


    @allure.step('Check that response is 200')
    def check_response_is_200(self):
        assert self.response.status == 200

    @allure.step('Check that 400 error')
    def check_bad_request(self):
        assert self.response.status_code == 400
