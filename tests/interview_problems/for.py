"""
1. Цикл for или генератор список (list comprehension)
"""

"""
1.1. Имеется список: numbers = [8, -1, 1, 4, 3, 6]
Создайте новый список со значениями из списка numbers, возведёнными в квадрат.
"""
# numbers = [8, -3, 1, 4, 3, 6, 9]
# numbers_sq = []
# for num in numbers:
#     numbers_sq.append(abs(num) ** 2)
# print(numbers_sq)

"""
То же самое с помощью генератора списков
"""
# numbers = [8, -1, 1, 4, 3, 6]
# numbers = [abs(num) ** 2 for num in numbers]
# print(*numbers)


"""
1.2. Имеется список: numbers = [82, -19, 7, 4, -3, 6, 29, 0, -94, 103]
Создайте новый список со значениями из списка numbers, которые являются чётными. Ноль пропускаем.
"""
# numbers = [82, -19, 7, 4, -3, 6, 29, 0, -94, 103]
# numbers_even = []
# for num in numbers:
#     if num == 0:
#         continue
#     if num % 2 == 0:
#         numbers_even.append(num)
# print(numbers_even)

"""
То же самое с помощью генератора списков
"""
numbers = [82, -19, 7, 4, -3, 6, 29, 0, -94, 103]
numbers_even = [num for num in numbers if num % 2 == 0 and num != 0]
print(numbers_even)


