#Напишите тесты на CRUD для https://petstore.swagger.io/user.
#При реализации учитывайте POM и Фабрик модели.
#DOD:
# 1) Тесты запускаются
# 2) Валидируют статус код ответа.
# 3) Проверка тела ответа
# ДЛЯ ЭТОЙ ЗАДАЧИ НЕОБХОДИМО ЗАПУСТИТЬ РЕДАКТОР КОДА И ДЕМОНСТРАЦИЮ ЭКРАНА. (30 минут)
import json
from random import random

import requests

URL = 'https://petstore.swagger.io/v2/user'
payload = {
  "id": 0,
  "username": "User1",
  "firstName": "string",
  "lastName": "string",
  "email": "string",
  "password": "string",
  "phone": "string",
  "userStatus": 0
}

response = requests.post(URL, json=payload)
response_json = response.json()

print(response)
print(response.json())

# assert 'code' in response.json()
assert response_json['code'] == 200
# assert response.status_code == 200


URL = 'https://petstore.swagger.io/v2/user/User1'
response = requests.get(URL)
response_json = response.json()
print(response.json())
assert response.status_code == 200
assert response_json['username']
