""""""
"""
Дан вложенный список: a = [1, 2, [55, 7, 88, [99, 111, 1077], 91], 44, 84]
Нужно получить и вывести число 111, используя индексацию.
"""
# a = [1, 2, [55, 7, 88, [99, 111, 1077], 91], 44, 84]
# result = a[2][0]
# print(result)


"""
Подсчитайте количество элементов в списке и выведите получившееся число.
numbers = [1, True, 6, None, [1, 3, 6], 'Стол', 3, 'Карандаш', 9]
"""
# lst = [1, True, 6, None, [1, 3, 6], 'Стол', 3, 'Карандаш', 9]
# lst_count = len(lst)
# print(lst_count)


"""
Выведите минимальное, максимально число и сумму всех введённых чисел
"""
# users = list(map(int, input().split()))
# print(f'{max(users)} {min(users)} {sum(users)}')


"""
Выведите введённые пользователем числа в порядке убывания
"""
# users = list(map(int, input().split()))
# users = sorted(users, reverse=True)
# print(*users)


"""
Выведите введённые пользователем числа в порядке возрастания
"""
# users = list(map(int, input().split()))
# users = sorted(users)
# print(*users)


""" 
Преобразуйте список в прописные буквы
words = ["hello", "world", "python"]
"""
"""Вместо исходного списка"""
# words = ["hello", "world", "python"]
# upper_words = [word.upper() for word in words]
# print(upper_words)

"""В новый список"""
# words = ["hello", "world", "python"]
# upper_words = []
# for word in words:
#     upper_words.append(word.upper())
# print(words)


"""
Верните список из квадратов чётных чисел в диапазоне от 0 до 9
"""
# even_squares = [x * x for x in range(10) if x % 2 == 0]
# print(even_squares)


"""
Определите, присутствует ли число 58 в данном списке. Если да, верните "True", в противном случае "False"
"""
# numbers_list = [1,2,3,7,99,2,3,77,907,99,2,3,1,2,1,3,5,4,6,5]
# print(58 in numbers_list)








# s = input()
# lst = s.split()
# cities = ["Москва", "Тверь", "Вологда"]
# lst.extend(cities)
# # lst = lst + cities
# print(*lst)



#
# s = input()
# lst = s.split()
# cities = ["Москва", "Тверь", "Вологда"]
# lst = cities + lst
# print(*lst)


#




# name = input()
# writer = input()
# number_pages = int(input())
# price = float(input())
# book = [name, writer, number_pages, price]
# del(book[2])
# book[1] = "Пушкин"
# book[-1] = book[-1] * 2
# print(book)

# marks = list(map(int, input().split()))
# print(f'{sum(marks) / len(marks):.1f}')

# cities = input().split()
# print(cities[-1])

# cities = input().split()
# a = 'Москва'
# print(a in cities)

# s = input()
# s1 = s.split()
# lst = list(map(int, s1))
# lst = list(map(int, input().split()))
# print(lst)


# t = [["Скажи-ка", "дядя", "ведь", "не", "даром"],
#      ["Я", "Python", "выучил", "с", "каналом"],
#      ["Балакирев", "что", "раздавал?"]]
#
# word = input()
# print(word in t[0] or word in t[1] or word in t[2])

# a = [True, [1, 0, ["True", ["Истина", "Ложь"], "F"]], False]
# print(a[1][2][2])

# r1 = input()
# r2 = input()
# r3 = input()
#
# general_list = []
# r1list = list(r1.split())
# r2list = list(r2.split())
# r3list = list(r3.split())
#
# general_list.append(r1list + r2list + r3list)
# print(r1list[3], r2list[3], r3list[3])
# print(general_list)

# s1 = input()
# s2 = input()
# s3 = input()
# print(list(s1))

# s1 = input()
# s2 = input()
# s3 = input()
# lst = []
# s1new = s1.split(" ")
# s2new = s2.split(" ")
# s3new = s3.split(" ")
# lst.append(s1new)
# lst.append(s2new)
# lst.append(s3new)
# print(lst)

# squares = list(map(lambda x: x**2, [1, 2, 3]))
# print(squares)



# lst = [5.4, 6.7, 10.4]
# digs = list(map(int, input().split()))
# lst.append(digs)
# print(lst)

# import pytest

# a1 = [1, 2, [55, 7, 88, [99, 111, 1077], 91], 44, 84]
# print(a1[2][3][2])


# my_list = [i*i for i in range(10)]
# print(my_list)
#
# squares = [x * x for x in range(5)]
# print(squares)
#
# plus = [x + x for x in range(5)]
# print(plus)

# even_squares = [x * x for x in range(10) if x % 2 == 0]
# print(even_squares)



# squares = (x * x for x in range(10))
# print(squares)         # <generator object ...>
# print(next(squares))   # 0
# print(next(squares))  # 1


# def search_python_tutorials():
#     # Заглушка для поиска
#     return ['Python tutorial', 'Python documentation', 'Python examples', 'Python tips']
#
#
# def test_search_results():
#     # Ожидаемые результаты поиска
#     expected_results = ['Python tutorial', 'Python documentation', 'Python examples']
#
#     # Фактические результаты (имитация поиска)
#     actual_results = search_python_tutorials()
#
#     # Проверяем, что все ожидаемые результаты присутствуют
#     for expected in expected_results:
#         assert expected in actual_results, f"Результат '{expected}' не найден"

    # # Проверяем количество результатов
    # assert len(actual_results) >= len(expected_results)


# expected_results = ['Python tutorial', 'Python documentation', 'Python examples']
# for i in expected_results:
#     print(i)

# list = [1,3,5,7]
# for i in list:
#     print(i)




