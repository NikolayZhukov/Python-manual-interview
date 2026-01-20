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


BASE_URL = 'https://petstore.swagger.io/v2/pet/'
pet_id = 333125

def add_new_pet():
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


# def update_pet_form_data():
#     url = f'{BASE_URL}{id}'
#     data = {
#         "name": "New Name 2"
#     }
#
#     response = requests.post(url, data=data)
#     print(f'update_form_data: {response.json()}')
#     assert response.status_code == 200
#
# update_pet_form_data()