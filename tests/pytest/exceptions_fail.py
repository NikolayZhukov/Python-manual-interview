from logging import raiseExceptions

import pytest
from requests.compat import integer_types

"""
Чем отличаются:
1. raise ValueError
2. try...except  
3. with pytest.raises(ValueError)
"""


# БАЗОВЫЙ PYTHON
# def divide(a, b):
#     if b == 0:
#         # raise ValueError("Деление на ноль не допускается")
#         raise Exception("Деление на ноль не допускается")
#         # raise ZeroDivisionError("Деление на ноль не допускается")
#     return a / b
#
# print(divide(8,0))


# # БАЗОВЫЙ PYTHON
# def divide(a, b):
#     try:
#         result = a / b
#     except Exception as e:
#         return f"Ошибка {e}: Деление на ноль не допускается"
#     else:
#         return result
#
# print(divide(8, 0))





# # PYTEST
# def divide(a, b):
#     # if b == 0:
#         # raise ValueError("Деление на ноль не допускается")
#         # raise Exception("Деление на ноль не допускается")
#     return a / b
#
# # Тест с использованием pytest.raises
# def test_divide_by_zero():
#     # with pytest.raises(ValueError):
#     with pytest.raises(Exception):
#         divide(10, 0)


"""
Задание:
Напиши функцию get_age(age), которая принимает число и:
если age < 0 или age > 120, выбрасывает ValueError("Некорректный возраст!"),
иначе возвращает строку "Ваш возраст: X".
"""

# age_user = int(input())
#
# def get_age(age):
#     if age < 0 or age > 120:
#         raise ValueError('Некорректный возраст')
#     else:
#         return f'Ваш возраст: {age}'
#
# print(get_age(age_user))



"""
Задание:
Попроси пользователя ввести число, и попробуй преобразовать ввод в int.
Если введено не число — выведи сообщение "Ошибка: введите целое число!".
Если всё хорошо — выведи "Вы ввели число X".
"""

def validate_input():
    while True:
        try:
            user_input = input('Введите любое целое число: ')
            user_input = int(user_input)
        except ValueError:
            print(f'Ошибка: введите целое число!')
            continue
        else:
            return f'Вы ввели число {user_input}'

print(validate_input())



