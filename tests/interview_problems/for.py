"""
1. Цикл for или генератор список (list comprehension), списковое включение
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
# numbers = [82, -19, 7, 4, -3, 6, 29, 0, -94, 103]
# numbers_even = [num for num in numbers if num % 2 == 0 and num != 0]
# print(numbers_even)

"""
1.3. Имеется список слов:
words = ["яблоко", "кот", "программирование", "собака", "электричество"]
Напишите функцию, которая принимает этот список и возвращает новый список с самыми длинными словами.
"""
# def find_longest_words(words):
#     words_sorted = sorted(words, key=len, reverse=True)
#     longest_word = words_sorted[0]
#     words_longest_lst = []
#     for word in words_sorted:
#         if word == longest_word:
#             words_longest_lst.append(word)
#     return words_longest_lst
#
# words = ["яблоко", "кот", "программирование", "собака", "электричество"]
# print(find_longest_words(words))

"""
То же самое с помощью генератора списков
"""

# def find_longest_words(words):
#     words_sorted = sorted(words, key=len, reverse=True)
#     longest_word = words_sorted[0]
#     words_longest_lst = [word for word in words_sorted if word == longest_word]
#     return words_longest_lst
#
# words = ["яблоко", "кот", "программирование", "собака", "электричество"]
# print(find_longest_words(words))


"""
1.4. Имеется список слов:
words = ["яблоко", "кот", "программирование", "собака", "электричество"]
Создайте новый список, в котором вместо каждого слова будет указано количество букв в данном слове.
"""
# words = ["яблоко", "кот", "программирование", "собака", "электричество"]
# words_len = []
# for word in words:
#     words_len.append(len(word))
#
# print(words_len)

"""
То же самое с помощью генератора списков
"""
# words = ["яблоко", "кот", "программирование", "собака", "электричество"]
# words_len = [len(word) for word in words]
# print(words_len)