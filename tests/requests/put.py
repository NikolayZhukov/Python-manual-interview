import requests
import uuid
unique_value = uuid.uuid4().hex

"""
POST
1. Название функции - через нижнее подчёркивание
2. Тело запроса - body
3. Переменная response
4. Из класса requests используем встроенный метод post 
5. У метода post должно быть два аргумента: 1) url 2) json=body
6. У reponse есть методы через точку - status_code, json()
"""


base_url = 'https://petstore.swagger.io/v2/pet/'


def update_pet_put_request():
    url = f'{base_url}'
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

    response = requests.put(url, json=body)
    assert response.status_code == 200
    print('\nResponse JSON:\n', response.json())

update_pet_put_request()