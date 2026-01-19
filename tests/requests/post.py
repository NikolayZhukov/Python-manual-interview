import requests
import uuid
unique_value = uuid.uuid4().hex

"""
POST
1. self - в скобочках
2. название - через нижнее подчёркивание
3. тело запроса - body
4. переменная response
5. из класса requests используем встроенный метод post 
6. у метода post должно быть два аргумента: 1) self.url 2) json=body
7. у reponse есть методы через точку - status_code, json()
"""


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