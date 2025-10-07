'''
Очистка окружения с помощью фикстуры
'''

"""
В pytest это делается через yield внутри фикстуры: 
всё, что идёт до yield, выполняется до теста, 
а всё, что идёт после — это teardown (очистка).
"""


import pytest
import os

@pytest.fixture
def temp_file():
    # setup: создаём временный файл
    filename = "temp.txt"
    with open(filename, "w") as f:
        f.write("hello")

    # передаём имя файла в тест
    yield filename

    # teardown: удаляем файл после теста
    if os.path.exists(filename):
        os.remove(filename)


def test_temp_file_exists(temp_file):
    # тест получает temp_file = "temp.txt"
    assert os.path.exists(temp_file)
