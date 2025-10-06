import pytest

# run_tests.py
import subprocess
import sys
from datetime import datetime




"""Пример использования raise ValueError без pytest"""
def calculate_age(birth_year):
    if birth_year > 2024:
        raise ValueError("Год рождения не может быть в будущем")
    if birth_year < 1900:
        raise ValueError("Слишком старый год рождения")

    return 2024 - birth_year

# try:
#     age = calculate_age(2001)
#     print(f'Ваш возраст - {age}')
# except ValueError as e:
#     print(f"Ошибка: {e}")



def test_calculate_age_success():
    """Тест успешного расчета возраста"""
    result = calculate_age(2000)
    assert result == 24


def test_calculate_age_future_birth_year():
    """Тест на исключение для года из будущего"""
    with pytest.raises(ValueError) as error_found:
        calculate_age(2030)

    # Проверяем текст сообщения об ошибке
    assert str(error_found.value) == "Год рождения не может быть в будущем"


def test_calculate_age_too_old_birth_year():
    """Тест на исключение для слишком старого года"""
    with pytest.raises(ValueError) as error_found:
        calculate_age(1850)

    # Проверяем текст сообщения об ошибке
    assert str(error_found.value) == "Слишком старый год рождения"


def test_calculate_age_normal_cases():
    """Тест нескольких корректных случаев"""
    assert calculate_age(1990) == 34
    assert calculate_age(1985) == 39
    assert calculate_age(2010) == 14


def test_calculate_age_edge_cases():
    """Тест граничных случаев"""
    # Минимально допустимый год
    assert calculate_age(1900) == 124

    # Максимально допустимый год
    assert calculate_age(2024) == 0




# def division():
#     try:
#         a, b = map(int, input().split())
#         c = a / b
#     except ValueError:
#         print('Введите именно число, а не букву!')
#     except ZeroDivisionError:
#         print('Введите любое число кроме ноля! На ноль делить нельзя!')
#     else:
#         return c
#     finally:
#         print('Ждём вас снова!')
#
# division()


# try:
#     f = open("data.txt", "r")
#     content = f.read()
# except FileNotFoundError:
#     print("Файл не найден")
# except PermissionError:
#     print("Нет доступа к файлу")
# except:
#     print('Произошла ошибка')



# try:
#     x = int("2d2")   # вызовет ValueError
# except ValueError:
#     print("Неверное преобразование строки в число")
# else:
#     print("Преобразование прошло успешно", x)
# finally:
#     print("Закрываю ресурс")