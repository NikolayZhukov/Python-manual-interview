


# def outer_func(tp):
#     def inner_func(input_value):
#         if tp == 'list':
#             input_value = list(input_value)
#         else:
#             input_value = tuple(input_value)
#         return input_value
#     return inner_func
#
# k = input()
# m = map(int, input().split())
#
# t = outer_func(k)
# print(t(m))


# def outer_func(tag):
#     def inner_func(value_tag):
#         result = f'<{tag}>{value_tag}</{tag}>'
#         return result
#     return inner_func
#
# k = input()
# m = input()
#
# t = outer_func(k)
# print(t(m))



# def outer_func():
#     def inner_func(input_str):
#         result = f'<h1>{input_str}</h1>'
#         return result
#     return inner_func
#
# k = input()
# t = outer_func()
# print(t(k))


# def counter_add(n, start=0):
#     def increment_counter():
#         nonlocal start
#         nonlocal n
#         start += n
#         return start
#     return increment_counter
#
# k = int(input())
# cnt = counter_add(2, k)
# print(cnt())




# def counter_add(n, start=0):
#     def increment_counter():
#         nonlocal start
#         nonlocal n
#         start += n
#         return start
#     return increment_counter
#
# k = int(input())
# cnt = counter_add(2, k)
# print(cnt())



# def counter_add(start=0):
#     def increment_counter():
#         nonlocal start
#         start += 5
#         return start
#     return increment_counter
#
# k = int(input())
# cnt = counter_add(k)
# print(cnt())



# def counter(start=0):
#     def step():
#         nonlocal start
#         start += 1
#         return start
#
#     return step
#
# c1 = counter()
# c2 = counter(3)
# c3 = counter(6)
# c4 = counter(9)

# print(c1(), c2(), c3(), c4())
# print(c1(), c2(), c3(), c4())
# print(c1(), c2(), c3(), c4())






# def say_name(name):
#     def say_goodbye():
#         print("Don't say me goodbye, " + name + "!")
#
#     return say_goodbye
#
# f = say_name("Sergey")
# f2 = say_name("Python")
# f()
# f2()
#
# def say_name(name):
#     return ("Don't say me goodbye, " + name + "!")
# f = print(say_name("Sergey"))
# f2 = print(say_name("Python"))

# f()
# f2()


# def create_global(x):
#     global TOTAL
#     TOTAL = x
#     return TOTAL
#
#
# WIDTH = int(input())
# def func1():
#     global WIDTH
#     # WIDTH = 13
#     return WIDTH
# print(func1())


# call_count = 0
#
# def counter():
#     global call_count
#     call_count += 1
#     return call_count
#
# print(counter())  # 1
# print(counter())  # 2
# print(counter())  # 3
# print(f"Функция вызвана {call_count} раз")


# s = input()
# element = lambda x, s: True if x in s else False
# print(element('ra', s))


# x = float(input())
#
# abs_func = lambda x: abs(x)
# print(abs_func(x))



# get_sq = lambda x: x ** 2


# get_div = lambda a, b: a / b if b != 0 else None

# lst_c = input().split()
# print(*lst_c,)
#
# cities = input().split()
# lst_c = (*cities,)
# print(lst_c)


# def get_biggest_city(*args):
#     return max(args, key=len)
# print(get_biggest_city('Питер', 'Москва', 'Самара', 'Воронеж'))



# def get_even(*args):
#     even_list = [num for num in args if num % 2 == 0]
#     return even_list



# digs = list(map(int, input().split()))
# a1 = max(digs)
# b1 = min(digs)
#
# def multiply(a, b):
#     sum = a * b
#     return sum
#
# print(multiply(a1, b1))


# cities = input().split()
#
# def get_cities(value):
#     length_value = len(value)
#     return value, length_value   # кортеж (город, длина)
#
# # словарь: ключ = город, значение = его длина
# d = {city: get_cities(city)[1] for city in cities}
#
# # сортировка ключей по значениям (длине города)
# a = sorted(d, key=d.get)
# print(*a)



# cities = input().split()
#
# def filter_cities(x):
#     if len(x) >= 6:
#         return True
#
# lst = [city for city in cities if filter_cities(city)]
# print(*lst)



# tp = input().strip()
#
# if tp == 'RECT':
#     def get_sq(a, b):
#         return a * b
# else:
#     def get_sq(a):
#         return a * a


# tp = input().strip()
# len_input = True if tp == 'RECT' else False
#
# def get_sq(a, b):
#     return a * b if len_input else a ** 2

# print(get_sq())



# def odd(x):
#     return x % 2 == 1   # True, если нечетное; False, если четное
#
# lst_d = list(map(int, input().split()))
#
# lst = [num for num in lst_d if odd(num)]
#
# print(*lst)
#
#
# def odd(x):
#     return x % 2 == 1   # True, если нечетное; False, если четное
#
# lst_d = list(map(int, input().split()))
#
# lst = []
# for num in lst_d:       # перебираем все элементы
#     if odd(num):        # проверяем на нечетность
#         lst.append(num) # добавляем в новый список
#
# print(*lst)


# def not_even(y):
#     return y % 2 == 1
# lst_d = list(map(int, input().split()))
# lst = []
#
# for x in lst_d:
#     if not_even(x):
#         lst.append(x)
# print(*lst)




# def even(y):
#     return y % 2 == 0   # True, если чётное; False, если нечётное
#
# # запускаем цикл ввода
# while True:
#     x = int(input())    # читаем число
#     if x == 1:          # условие выхода
#         break
#     if even(x):         # проверка через функцию
#         print(x)

# def is_large(input_str):
#     return False if len(input_str) < 3 else True




# def is_triangle(a, b, c):
#     return True if a < b + c and b < a + c and c < a + b else False


# def get_sq(x: float):
#     sq = x ** 2
#     return sq
#
# user_input = float(input())
# print(get_sq(user_input))



# import re
#
# def check_email(email: str):
#     pattern = r"^(?=.*@)(?=.*\.)[A-Za-z0-9_@.]+$"
#     if re.fullmatch(pattern, email):
#         print("ДА")
#     else:
#         print("НЕТ")
#
# user_input = input()
# check_email(user_input)

# def outer():
#     x = 10  # переменная внешней функции
#
#     def inner():  # это ЗАМЫКАНИЕ - оно "запоминает" x
#         return x + 5  # использует переменную из внешней области
#     return inner
#
# closure = outer()
# print(closure())

""""""
"""Замыкание"""

# def outer(b):
#     x = 10  # переменная внешней функции
#
#     def inner():  # это ЗАМЫКАНИЕ - оно "запоминает" x
#         return x + b  # использует переменную из внешней области
#     return inner
#
# closure = outer(7)
# print(closure())


"""Счётчик-замыкание nonlocal"""


def counter():
    count = 0

    def increment():
        nonlocal count
        count += 1
        return count

    return increment


c = counter()
print(c())  # 1 - outer() завершена, но count жив!
print(c())  # 2
print(c())  # 3
print(c())  # 3
print(c())  # 3

# def calculate_list(lst1):
#     v_min = min(lst1)
#     v_max = max(lst1)
#     v_sum = sum(lst1)
#     print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')
#
# lst_input = list(map(int, input().split()))
# calculate_list(lst_input)





# def weight_thing(x: float):
#     print(f'Предмет имеет вес: {x} кг.')
#
# user_input=float(input())
# weight_thing(user_input)



# def print_frase():
#     name, surname, *rest = input().split()
#     print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")
#
# print_frase()


# d = {'Москва':6, 'Питер':5, 'Воронеж':7}
# print(max(d, key=d.get))

