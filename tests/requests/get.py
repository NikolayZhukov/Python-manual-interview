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

class TestAccountAuthorized:
    url = 'https://demoqa.com/Account/v1/Authorized'

    def test_login_200(self):
        body = {
            "userName": "Nikolay_tester",
            "password": "Tester123!"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 200
        payload = response.json()
        assert payload is True

    # 1) Почему здесь payload = response.json(), если здесь bool, True?

    def test_login_400(self):
        body = {
            "userName": "1"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 400
        payload = response.json()
        assert payload['message'] == 'UserName and Password required.'

    def test_login_404(self):
        body = {
            "userName": "string",
            "password": "string"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 404
        payload = response.json()
        assert payload['message'] == 'User not found!'


# 2) Почему здесь возвращает 404? Ошибка 404 возникает,
# когда пользователь или поисковая система обращаются к несуществующей странице,
# удалённому контенту или недоступному файлу

class TestAccountGenerateToken:
    url = 'https://demoqa.com/Account/v1/GenerateToken'

    def test_200(self):
        body = {
            "userName": "string",
            "password": "string"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 200
        payload = response.json()
        assert payload['result'] == 'User authorization failed.'

    def test_400(self):
        body = {
            "userName": 1,
            "password": 1
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 400
        payload = response.json()
        assert payload['message'] == 'string'


class TestAccountUser:
    url = 'https://demoqa.com/Account/v1/User'

    def test_201(self):
        body = {
            "userName": f"{unique_value}",
            "password": "Tester_123!!!"
        }

        response = requests.post(self.url, json=body)
        print(f' userName = {unique_value}')

        assert response.status_code == 201

        payload = response.json()
        assert payload['username'] == f'{unique_value}'

    def test_404(self):
        self.url = 'https://demoqa.com/Account/v1/User222'
        body = {
            "userName": "S",
            "password": "S"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 404

        # payload = response.json()
        # assert payload['message'] == 'User not found!'

    def test_406(self):
        body = {
            "userName": "User_1",
            "password": "User_Pass1!!"
        }

        response = requests.post(self.url, json=body)

        assert response.status_code == 406

        payload = response.json()
        assert payload['message'] == 'User exists!'


class TestAccountDelete:
    unique_value_user = []
    def test_201(self):
        self.url = 'https://demoqa.com/Account/v1/User'
        body = {
            "userName": f"{unique_value}",
            "password": "Tester_123!!!"
        }

        response = requests.post(self.url, json=body)
        print(f'"userName": f"{unique_value}"')

        return unique_value



    def test_200(self):
        self.url = f'https://demoqa.com/Account/v1/User/{unique_value}'

        response = requests.delete(self.url)

        assert response.status_code == 200

        # payload = response.json()
        # assert payload['username'] == f'{unique_value}'

    def test_401(self):
        self.url = f'https://demoqa.com/Account/v1/User/{unique_value}'

        response = requests.delete(self.url)

        assert response.status_code == 401

        # payload = response.json()
        # assert payload['username'] == f'{unique_value}'


class TestGetUserInfo:
    def test_200(self):
        self.url = f'https://demoqa.com/Account/v1/User/{unique_value}'

        response = requests.get(self.url)

        assert response.status_code == 200