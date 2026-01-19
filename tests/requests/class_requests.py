import requests
BASE_URL = 'https://petstore.swagger.io/v2/pet/'
pet_id = 333125

class TestPetStoreRequests():
    def test_add_new_pet(self):
        self.url = f'{BASE_URL}'
        body = {
            "id": pet_id,
            "category": {
                "id": 0,
                "name": "string"
            },
            "name": "Dog Test 1",
            "photoUrls": [
                "string"
            ],
            "tags": [
                {
                    "id": 0,
                    "name": "string"
                }
            ],
            "status": "available"
        }

        response = requests.post(self.url, json=body)
        print(f'\nrequest_body: {body}')
        assert response.status_code == 200
        print('\nResponse JSON:', response.json())

    def test_update_pet_form_data(self):
        self.url = f'{BASE_URL}{pet_id}'
        data = {
            "name": "New Name 2"
        }

        response = requests.post(self.url, data=data)
        print(f'\nrequest_data: {data}')
        assert response.status_code == 200

    def test_find_pet_by_id(self):
        self.url = f'{BASE_URL}{pet_id}'
        response = requests.get(self.url)

        payload = response.json()

        # print(f'request = {response.request}')
        # print(f'json = {response.json()}')
        # print(f'status code = {response.status_code}')
        # print(f'text = {response.text}')
        # print(f'content = {response.content}')
        # print(f'headers = {response.headers}')
        # print(f'url = {response.url}')
        # print(f'elapsed time = {response.elapsed}')
        # print(f'encoding = {response.encoding}')
        # print(f'cookies = {response.cookies}')

        print(f'payload: {payload}')
        # print(f'payload_id: {payload["id"]}')
        # print(f'payload_name: {payload["name"]}')
        # print(f'payload_tags: {payload["tags"]}')
        # print(f'payload_tags_id: {payload["tags"][0]["id"]}')
        # print(f'payload_category_id: {payload["category"]["id"]}')

        assert response.status_code == 200
        # return f'payload_category_id: {payload["category"]["id"]}'

    def test_delete_pet_by_id(self):
        self.url = f'{BASE_URL}{pet_id}'
        response = requests.delete(self.url)
        payload = response.json()
        print(response.json())
        print(f'message: {payload["message"]}')

    def test_find_pet_by_id_after_delete(self):
        self.url = f'{BASE_URL}{pet_id}'
        response = requests.get(self.url)

        payload = response.json()

        print(f'payload: {payload}')
        print(f'message: {payload["message"]}')


        assert response.status_code == 404
        assert payload["message"] == "Pet not found"
        # return f'payload_category_id: {payload["category"]["id"]}'











