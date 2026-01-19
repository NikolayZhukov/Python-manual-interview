import requests

base_url = 'https://petstore.swagger.io/v2/pet/'
id = 333125


def delete_pet_by_id():
    url = f'{base_url}{id}'
    response = requests.delete(url)
    payload = response.json()
    print(response.json())
    print(f'message: {payload["message"]}')
    # assert response.status_code == 200

delete_pet_by_id()