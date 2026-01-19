import requests
import uuid


base_url = 'https://petstore.swagger.io/v2/pet/'
id = '333125'


def find_pet_by_id():
    url = f'{base_url}{id}'

    response = requests.get(url)
    print(response.json())
    print(url)
    assert response.status_code == 200

if __name__ == "__main__":
    find_pet = find_pet_by_id()