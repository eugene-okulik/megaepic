from locust import task, HttpUser


class ApiUser(HttpUser):
    id = None

    def on_start(self):
        response = self.client.post(
            '/objects',
            json={
                "name": "Elbey",
                "data": {
                    "year": 2019,
                    "price": 1849.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB"
                }
            }
        )
        self.id = response.json()['id']

    @task
    def get_all_objects(self):
        self.client.get(
            '/objects',
            headers={"Content-Type": "application"}
        )

    @task
    def get_one_object_by_id(self):
        self.client.get(
            f'/objects/{self.id}',
            headers={"Content-Type": "application"}
        )

    @task
    def put_object_by_id(self):
        self.client.put(
            f'/objects/{self.id}',
            json={
                "name": "new_name",
                "data": {
                    "year": 2019,
                    "price": 2049.99,
                    "CPU model": "Intel Core i9",
                    "Hard disk size": "1 TB",
                    "color": "silver"
                }
            },
            headers={"Content-Type": "application"}
        )

    @task
    def delete_object_by_id(self):
        self.client.delete(
            f'/objects/{self.id}',
            headers={"Content-Type": "application"}
        )
