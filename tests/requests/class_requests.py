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
        assert response.status_code == 200
        print('\Response JSON:', response.json())

    def add_new_pet(self):
        url = f'{BASE_URL}'
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

        response = requests.post(url, json=body)
        assert response.status_code == 200
        print('\nResponse JSON:\n', response.json())

    add_new_pet()





