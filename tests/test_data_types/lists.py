# import pytest
#

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

# even_squares = [x * x for x in range(100) if x % 2 == 0]
# print(even_squares)

squares = (x * x for x in range(10))
print(squares)         # <generator object ...>
print(next(squares))   # 0
print(next(squares))  # 1

sum = 155
sum_repr =
print()


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

# numbers_list = [1,2,3,7,99,2,3,77,907,99,2,3,1,2,1,3,5,4,6,5]
# print(58 in numbers_list)


