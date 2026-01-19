import requests
import uuid

base_url = 'https://petstore.swagger.io/v2/pet/'
id = '333125'

"""
GET
1. Название функции - через нижнее подчёркивание
2. Переменная response
3. Из класса requests используем встроенный метод get
4. У метода post должен быть всего один аргумент - url
5. У reponse есть методы через точку - status_code, json()
6. Из ответа json можно получить значение отдельно взятого поля - payload["name"] - через 
квадратные скобки и в кавычках
7. Если нужно получить значение ключа из словаря, то просто добавляем вторые квадратные скобки 
со названием ключа - payload["category"]["id"]
8. Если нужно получить значение ключа словаря, который находится внутри списка, то ещё по середине 
добавляем индекс - если список всегод один, то индекс тоже нужен и он будет равен нулю - payload["tags"][0]["id"] 
9. Запуск через: 
   1) find_pet_by_id()
   2) print(find_pet_by_id()) - но в этом случае нужно в return указывать что возвращает
   3) if __name__ == '__main__': find_pet_by_id()
   4) Либо просто добавить в названии функции слово test_ и убрать find_pet_by_id(), но должен быть 
   установлен pytest 
"""


def find_pet_by_id():
    url = f'{base_url}{id}'
    response = requests.get(url)

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

    print(payload)
    # print(f'payload_id: {payload["id"]}')
    # print(f'payload_name: {payload["name"]}')
    # print(f'payload_tags: {payload["tags"]}')
    # print(f'payload_tags_id: {payload["tags"][0]["id"]}')
    # print(f'payload_category_id: {payload["category"]["id"]}')

    assert response.status_code == 200
    # return f'payload_category_id: {payload["category"]["id"]}'

# print(find_pet_by_id())
find_pet_by_id()