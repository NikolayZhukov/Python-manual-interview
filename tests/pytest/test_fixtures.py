import os
import pytest
import tempfile



def divide(a, b):
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю")
    return a / b


def test_divide_by_zero():
    with pytest.raises(ValueError) as exc_info:
        divide(10, 0)
    print(str(exc_info.value))

    # Проверка текста сообщения об ошибке
    assert str(exc_info.value) == "Делитель не может быть равен нулю"


def test_divide_success():
    result = divide(10, 2)
    assert result == 5



# Простые математические функции
# def add(a, b):
#     return a + b
#
# def subtract(a, b):
#     return a - b
#
# def multiply(a, b):
#     return a * b
#
# # Тестируем разные функции с разными параметрами
# @pytest.mark.parametrize("func,a,b,expected", [
#     (add, 2, 3, 5),
#     (add, -1, 1, 0),
#     (subtract, 5, 2, 3),
#     (subtract, 10, 10, 0),
#     (multiply, 4, 3, 12),
#     (multiply, 7, 0, 0),
# ])
# def test_math_operations(func, a, b, expected):
#     result = func(a, b)
#     assert result == expected
#
#
# Базовая функция для тестирования
# def calculate(a, b, operation):
#     if operation == 'add':
#         return a + b
#     elif operation == 'subtract':
#         return a - b
#     elif operation == 'multiply':
#         return a * b
#
# # Тест с parametrize
# @pytest.mark.parametrize("a,b,operation,expected", [
#     (2, 3, 'add', 5),
#     (5, 2, 'subtract', 3),
#     (4, 3, 'multiply', 12),
#     (0, 5, 'add', 5),
#     (10, 10, 'subtract', 0),
#     (7, 0, 'multiply', 1),
#     (5, 2, 'multiply', 10),
#     (5, 7, 'subtract', -2),
# ])
# def test_calculations(a, b, operation, expected):
#     result = calculate(a, b, operation)
#     assert result == expected, f"{a} {operation} {b} should be {expected}, got {result}"



# @pytest.mark.fast
# def test_addition():
#     assert 1 + 1 == 3
#
# @pytest.mark.slow
# def test_api_call():
#     assert True
#
# @pytest.mark.fast
# def test_subtraction():
#     assert 5 - 3 == 2
#
# @pytest.mark.integration
# def test_database():
#     assert True




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

# @pytest.fixture
# def sample_data():
#     print("\n1) Выполняется фикстура перед тестом")
#     data = [1, 2, 3]
#     yield data
#     print("\n3) Выполняется фикстура после теста")
#
#
# def test_sum(sample_data):
#     print("\n2) Выполняется сама функция")
#     assert sum(sample_data) == 6
#
#
# def test_len(sample_data):
#     print("\n2) Выполняется сама функция")
#     assert len(sample_data) > 0





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



