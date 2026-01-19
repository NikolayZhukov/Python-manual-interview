import requests
import uuid


base_url = 'https://petstore.swagger.io/v2/pet/'
id = '333125'


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
    print(f'payload_tags_id: {payload["tags"][0]["id"]}')
    print(f'payload_category_id: {payload["category"]["id"]}')

    # assert response.status_code == 200

if __name__ == "__main__":
    find_pet = find_pet_by_id()