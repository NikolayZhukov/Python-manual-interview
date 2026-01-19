import requests

BASE_URL = 'https://petstore.swagger.io/v2/pet/'
pet_id = 333125


def delete_pet_by_id():
    url = f'{}{pet_id}'
    response = requests.delete(url)
    payload = response.json()
    print(response.json())
    print(f'message: {payload["message"]}')
    # assert response.status_code == 200


delete_pet_by_id()