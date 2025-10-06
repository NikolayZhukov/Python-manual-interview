import os
import pytest
import tempfile


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return f"Person: {self.name}, {self.age}"  # Added "years old"
#
#     def __repr__(self):
#         return f"Person('{self.name}', {self.age})"
#
#
# person = Person("Alice", 25)
#
# print(str(person))   # Output: Person: Alice, 25 years old
# print(repr(person))  # Output: Person('Alice', 25)



# import pytest
#
# # фикстура
# @pytest.fixture
# def sample_data():
#     print("\nВыполняется фикстура перед тестом")  # выполняется перед тестом
#     data = [1, 2, 3]
#     return data
#
# # тест с использованием фикстуры
# def test_sum(sample_data):
#     assert sum(sample_data) == 6


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
    print("\n2) Выполняется сама функция")
    assert sum(sample_data) == 6


def test_len(sample_data):
    print("\n2) Выполняется сама функция")
    assert len(sample_data) > 0



# Пример 1: Работа с временными файлами
# @pytest.fixture
# def temp_file():
#     print("\nСоздаем временный файл")
#     # Создаем временный файл
#     temp = tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.txt')
#     temp.write("Hello, World!\nTest data")
#     temp.close()
#     file_path = temp.name
#
#     yield file_path
#
#     # Код после yield - удаляем временный файл
#     print("Удаляем временный файл")
#     if os.path.exists(file_path):
#         os.unlink(file_path)


