# def add_start(tag='h1'):
#     def decorator_func(func):
#         def wrapper(s):
#             result = func(s)
#             return f'<{tag}>{result}</{tag}>'
#         return wrapper
#     return decorator_func
#
#
# @add_start('div')
# def make_lower(s):
#     return s.lower()
#
# s = input()
# print(make_lower(s))



# def tag_decorator(tag="h1"):
#     def decorator(func):
#         def wrapper(s):
#             result = func(s)
#             return f"<{tag}>{result}</{tag}>"
#         return wrapper
#     return decorator

# @tag_decorator("div")
# def to_lowercase(s):
#     return s.lower()

# s = input()
# print(to_lowercase(s))


# num = input()

# def add_start(start):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             result = func(*args, **kwargs)
#             return result + start
#         return wrapper
#     return decorator
#
# @add_start(start=5)
# def sum_num(lst):
#     sum_number = sum(map(int, num.split()))
#     return sum_number
#
# print(sum_num(num))


# from functools import wraps
#
# def my_decorator(func):
#     @wraps(func)  # ← Вот он!
#     def wrapper(*args, **kwargs):
#         """Документация wrapper"""
#         print(f"Вызывается функция: {func.__name__}")
#         return func(*args, **kwargs)
#     return wrapper
#
# @my_decorator
# def hello(name):
#     """Приветствует пользователя"""
#     return f"Привет, {name}!"
#
# # Теперь метаданные сохранились
# print(hello.__name__)  # Вывод: hello ✅
# print(hello.__doc__)   # Вывод: Приветствует пользователя ✅
#
# # Функция работает как обычно
# result = hello("Анна")
# # Вывод: Вызывается функция: hello
# print(result)  # Вывод: Привет, Анна!


# def sort_func(func):
#     def wrapper(*args, **kwargs):
#         res = func(*args, **kwargs)
#         keys, values = res
#         d = {keys[i]: values[i] for i in range(len(keys))}
#         print(*sorted(d.items()))
#     return wrapper
#
# @sort_func
# def make_list(x, y):
#     lst_1 = x.split()
#     lst_2 = y.split()
#     tuple_conv = (lst_1, lst_2)
#     return tuple_conv
#
# line_1 = input()
# line_2 = input()
# make_list(line_1, line_2)



# def sort_func(func):
#     def wrapper(y):
#         lst_1 = func(y)
#         f_r = sorted(lst_1, )
#         return f_r
#     return wrapper
#
# @sort_func
# def make_list(x):
#     lst = list(x)
#     return lst
#
# num = map(int, input().split())
# print(*make_list(num))




# def show_menu(func):
#     def wrapper(s):
#         menu_list = func(s)
#         print(s)
#         print(menu_list)
#         for i, item in enumerate(menu_list, start=1):
#             print(f"{i}. {item}")
#         return menu_list
#     return wrapper
#
# @show_menu
# def get_menu(s):
#     return s.split()
#
# menu = input()
# get_menu(menu)


# def func_show(func):
#     def wrapper(width, height):
#         result = func(width, height)
#         print(f"Площадь прямоугольника: {result}")
#         return result
#     return wrapper
#
# @func_show
# def get_sq(width, height):
#     return width * height
#
# # Ввод и вызов в две строки
# width, height = map(int, input().split())
# get_sq(width, height)



# def func_show(func):
#     def wrapper(width, height):
#         result = func(width, height)
#         print(f"Площадь прямоугольника: {result}")
#         return result
#     return wrapper
#
# def get_sq(width, height):
#     return width * height