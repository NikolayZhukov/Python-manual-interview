import pytest
import os

"""
1. Пример фикстуры с yield, состоящий из трёх частей: 
1) Действие перед функцией
2) Сама функция
3) Действие после функции
"""

@pytest.fixture
def sample_data():
    print("\n1) Выполняется фикстура перед тестом")
    data = [1, 2, 3]
    yield data
    print("\n3) Выполняется фикстура после теста")


def test_sum(sample_data):
    print("\n2) Выполняется сама функция Сумма")
    assert sum(sample_data) == 6


def test_len(sample_data):
    print("\n2) Выполняется сама функция Длина")
    assert len(sample_data) > 0

def test_sum_divide_two(sample_data):
    print('\n3) Выполняется сама функция Умножение')
    assert sum(sample_data) / 2 == 3

def test_sum_divide_three(sample_data):
    print('\n3) Выполняется сама функция Умножение')
    assert sum(sample_data) / 3 == 2




''' Очистка окружения с помощью фикстуры '''

"""
В pytest это делается через yield внутри фикстуры: 
всё, что идёт до yield, выполняется до теста, 
а всё, что идёт после — это teardown (очистка).
"""



# @pytest.fixture
# def temp_file():
#     # setup: создаём временный файл
#     filename = "temp.txt"
#     with open(filename, "w") as f:
#         f.write("hello")
#
#     # передаём имя файла в тест
#     yield filename
#
#     # teardown: удаляем файл после теста
#     if os.path.exists(filename):
#         os.remove(filename)
#
#
# def test_temp_file_exists(temp_file):
#     # тест получает temp_file = "temp.txt"
#     assert os.path.exists(temp_file)
