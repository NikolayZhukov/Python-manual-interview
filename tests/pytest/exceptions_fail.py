from logging import raiseExceptions

import pytest
import requests
# from requests.compat import integer_types

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
# print(divide(8, 1))





# PYTEST
# def divide(a, b):
#     if b == 0:
#         # raise ValueError("Деление на ноль не допускается")
#         raise Exception("Деление на ноль не допускается")
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

"""
1 способ - с break
"""
# def validate_input():
#     while True:
#         try:
#             user_input = int(input('Введите любое целое число: '))
#             break
#         except ValueError:
#             print(f'Ошибка: введите целое число!')
#     return f'Вы ввели число {user_input}'
#
# print(validate_input())


"""
2 способ - с continue
"""
# def validate_input():
#     while True:
#         try:
#             user_input = input('Введите любое целое число: ')
#             user_input = int(user_input)
#         except ValueError:
#             print(f'Ошибка: введите целое число!')
#             continue
#         else:
#             return f'Вы ввели число {user_input}'
#
# print(validate_input())

"""
3 способ - без цикла while, с рекурсией (то есть функция вызывает саму себя)
"""
# def validate_input():
#         try:
#             user_input = input('Введите любое целое число: ')
#             user_input = int(user_input)
#         except ValueError:
#             print(f'Ошибка: введите целое число!')
#             return validate_input()
#         else:
#             return f'Вы ввели число {user_input}'
#
# print(validate_input())


"""
Напиши функцию get_positive_number(), которая:
Просит пользователя ввести число (целое или вещественное).
Если пользователь вводит не число — вывести сообщение:
"Ошибка: введите число!"
и попросить ввести заново.

Если число отрицательное или равно нулю — вывести сообщение:
"Ошибка: нужно положительное число!"
и попросить ввести снова.

Когда введено корректное положительное число —
вывести "Ваше число: X" и завершить работу.
"""
"""
1 способ - try ... except
"""
# def get_positive_number():
#     while True:
#         try:
#             user_input = float(input('Введите любое число: '))
#             if user_input > 0 and user_input != 0:
#                 break
#             else:
#                 print(f'Ошибка: введите число больше ноля и не равное нолю')
#         except ValueError:
#             print(f'Ошибка: введите число больше нуля и не равное нулю')
#     print(f'Вы ввели число {user_input}')

# get_positive_number()



"""
Задание:
Напиши функцию get_password(), которая:

Просит пользователя ввести пароль.

Если длина пароля меньше 8 символов, вывести сообщение:
"Ошибка: пароль слишком короткий!"
Если длина пароля больше 20 символов, вывести сообщение:
"Ошибка: пароль слишком длинный!"
и попросить ввести снова.

Когда пароль подходит под оба условия — вывести сообщение:
"Пароль принят!" и завершить программу.
"""

"""
1 способ
"""
# def get_password():
#     while True:
#         password_input = input("Введите пароль от 8 до 20 символов: ")
#         if len(password_input) < 8:
#             print("Ошибка: пароль слишком короткий!")
#         elif len(password_input) > 20:
#             print("Ошибка: пароль слишком длинный!")
#         else:
#             print("Пароль принят!")
#             break
#
# get_password()

"""
2 способ - двойная проверка, излишне, но работает
"""
# def get_password():
#     while True:
#         password_input = input("Введите пароль от 8 до 20 символов: ")
#         if 8 <= len(password_input) <= 20:
#             break
#         else:
#             if len(password_input) < 8:
#                 print("Ошибка: пароль слишком короткий!")
#             if len(password_input) > 20:
#                 print("Ошибка: пароль слишком длинный!")
#     print("Пароль принят!")
#
# get_password()


"""
Напиши функцию get_positive_list(), которая:
Просит пользователя ввести 5 чисел через пробел (например: 1 -3 4 0 7).
Разбивает введённую строку на отдельные элементы и превращает их в числа
Проверяет, что все числа больше нуля.
Если встречается отрицательное число или ноль — вывести сообщение
"Ошибка: все числа должны быть положительными!"
и попросить ввести заново.
Если все числа положительные — вывести:
"Список принят!"
и завершить программу (break).
"""

# def get_positive_list():
#     while True:
#         user_input = list(map(int, input("Введите 5 чисел больше нуля через пробел: ").split()))
#
#         if len(user_input) != 5:
#             print("Ошибка: нужно ввести ровно 5 чисел!")
#             continue
#
#         list_verify = []
#         for i in user_input:
#             if i > 0:
#                 list_verify.append(i)
#             else:
#                 print("Ошибка: все числа должны быть больше нуля!")
#                 list_verify = []  # сбросим, чтобы не сохранять частично верные
#                 break
#
#         if len(list_verify) == 5:  # все числа положительные
#             print("Ваш список принят!")
#             break
#
# get_positive_list()


"""
Напиши функцию check_words_length(), которая:
Просит пользователя ввести 1 слово не короче 3 символов.

Если какое-то слово короче — вывести сообщение
"Ошибка: все слова должны быть длиной не меньше 3 символов!"
и попросить ввести снова.

Если все слова достаточно длинные — вывести
"Все слова приняты!" и завершить программу (break).
"""

# def check_words_length():
#     list_final = []
#
#     while len(list_final) < 3:
#         word = input(f"Введите слово не меньше 3 букв: ")
#         if len(word) < 3:
#             print("Ошибка: слово слишком короткое!")
#             continue
#         else:
#             list_final.append(word)
#
#     print("Ваши слова приняты:", list_final)
#
# check_words_length()






