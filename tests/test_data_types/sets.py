
# import sys
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# lst_in = set(lst_in)
# print(len(lst_in))




# # Читаем входную строку
# s = input()
#
# # Множество для хранения уникальных цифр
# unique_digits = set()
#
# # Проходим по каждому символу строки
# for char in s:
#     # Проверяем, является ли символ цифрой
#     if char.isdigit():
#         unique_digits.add(char)
#
# # Если нашлись цифры
# if unique_digits:
#     # Преобразуем в список и сортируем
#     sorted_digits = sorted(unique_digits)
#     # Выводим через пробел
#     # print(' '.join(sorted_digits))
#     print(*sorted_digits)
# else:
#     # Если цифр нет
#     print("НЕТ")


# words = list(input().split())
# words = " ".join(words)
# words = words.lower()
# words = list(words.split())
#
# words_unique = set(words)
# print(len(words_unique))



# s1 = list(map(float, input(). split()))
# s = set(s1)
# print(*sorted(s))




# fruits_set = {'apple', 'banana', 'cherry'}
# print(fruits_set)

# numbers = {1,2,3,7,99}
# print(type(numbers))
#
# numbers = {}
# print(type(numbers))
#
# numbers = set()
# print(type(numbers))

# numbers_list = [1,2,3,7,99,2,3,77,907,99,2,3,1,2,1,3,5,4,6,5]
# numbers_set = set(numbers_list)
# numbers_list_unique = list(numbers_set)
# print(type(numbers_set))
# print(numbers_set)
# print(numbers_list)
# print(numbers_list_unique)

# numbers_list = [1,2,3,7,99,2,3,77,907,99,2,3,1,2,1,3,5,4,6,5]
# numbers_set = set(numbers_list)
# for i in numbers_set:
#     print(i)

# numbers = {1,2,3,7,99}
# print(1 in numbers)

