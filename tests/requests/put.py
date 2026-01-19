import requests
import uuid
unique_value = uuid.uuid4().hex

base_url = 'https://petstore.swagger.io/v2/pet/'

def test_update_pet_put_request(self):
    self.url = f'{base_url}'
    body = {
        "id": 333125,
        "category": {
            "id": 0,
            "name": "string"
        },
        "name": "Dog Test 999",
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

    response = requests.put(self.url, json=body)
    assert response.status_code == 200
    print('\nResponse JSON:\n', response.json())