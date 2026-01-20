import requests
import pytest

base_url = 'https://petstore.swagger.io/v2/pet/'

class TestAddNewPet:
    def test_add_new_pet(self):
        self.url = f'{base_url}'
        body = {
                "id": 333125,
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
        print('\nResponse JSON:\n', response.json())