import pytest

"""
Чем отличаются:
1. raise ValueError
2. try...except  
3. with pytest.raises(ValueError)
"""


# БАЗОВЫЙ PYTHON
# def divide(a, b):
#     if b == 0:
#         raise ValueError("Деление на ноль не допускается")
#     return a / b
#
# print(divide(8,0))


# # БАЗОВЫЙ PYTHON
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "Ошибка: Деление на ноль не допускается"
#
# print(divide(8, 0))


# # PYTEST
def divide(a, b):
    if b == 0:
        raise ValueError("Деление на ноль не допускается")
    return a / b

# Тест с использованием pytest.raises
def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)