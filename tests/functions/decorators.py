"""Декораторы"""

""" 
Оглавление 
1. Структура декораторов
2. Два способа декорирования функции
3. Максимально универсальный декоратор - сколько угодно аргументов: *args, **kwargs
4. Декораторы с аргументами
5. Декоратор метода в классе - с передачей self
"""


""" 1. Структура декораторов: 
- без передачи аргументов в декораторы, 
- здесь аргументы передаются только в саму декорируемую функцию"""


# def uppercase(func):
#     def wrapper():
#         return func().upper()
#     return wrapper
#
# @uppercase
# def hello():
#     return "hello"
#
# print(hello())


# def decorator_func(func):
#     def wrapper_func(a, b):
#         result = func(a, b)
#         print('До декорируемой функции')
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# @decorator_func
# def calculate_area_rectangle(length, width):
#     return length * width
#
# print(calculate_area_rectangle(user_input_length, user_input_width))


""" 2. Два способа декорирования функции"""

"""1 способ - передать саму функцию в декоратор (без скобочек и аргументов)"""
# def decorator_func(func):
#     def wrapper_func(a, b):
#         result = func(a, b)
#         print('До декорируемой функции')
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# def calculate_area_rectangle(length, width):
#     return length * width
#
# calculate_area_rectangle = decorator_func(calculate_area_rectangle)
# calculate_area_rectangle(user_input_length, user_input_width)


"""2 способ - с помощью @decorator_function над декорируемой функцией"""

# def decorator_func(func):
#     def wrapper_func(a, b):
#         result = func(a, b)
#         print('До декорируемой функции')
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# @decorator_func
# def calculate_area_rectangle(length, width):
#     return length * width
#
# calculate_area_rectangle(user_input_length, user_input_width)



""" 3. Максимально универсальный декоратор - сколько угодно аргументов или без аргументов"""
# def decorator_func(func):
#     def wrapper_func(*args, **kwargs):
#         result = func(*args, **kwargs)
#         print('До декорируемой функции')
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
# @decorator_func
# def calculate_area_rectangle(length, width):
#     return length * width
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# calculate_area_rectangle(user_input_length, user_input_width)


""" 4. Декораторы с аргументами"""
# def decorator_func_with_args(show_before, show_after):
#     def decorator_func(func):
#         def wrapper_func(a, b):
#             if show_before:
#                 print('До декорируемой функции')
#             result = func(a, b)
#             print('Результат =', result)
#             if show_after:
#                 print('После декорируемой функции')
#             return result
#         return wrapper_func
#     return decorator_func
#
# @decorator_func_with_args(show_before=True, show_after=True)  # передаем аргументы в декоратор
# def calculate_area_rectangle(length, width):
#     return length * width
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# calculate_area_rectangle(user_input_length, user_input_width)



""" 5. Декоратор метода в классе - с передачей self"""

# def decorator_func(func):
#     def wrapper_func(self, a, b):
#         print(f'--- Прямоугольник {self.color} ---')
#         print('До декорируемой функции')
#         result = func(self, a, b)
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
#
# class Rectangle:
#     def __init__(self, color):
#         self.length = None
#         self.width = None
#         self.color = color
#
#     def input_dimensions(self):
#         print(f"\nВведите размеры для {self.color} прямоугольника:")
#         self.length = int(input("Длина: "))
#         self.width = int(input("Ширина: "))
#
#     @decorator_func
#     def calculate_area_rectangle(self, length, width):
#         return length * width
#
#     def calculate_area(self):
#         return self.calculate_area_rectangle(self.length, self.width)
#
#
# # Запрос у пользователя количества прямоугольников
# num_rectangles = int(input("Сколько прямоугольников хотите создать? "))
#
# rectangles = []
#
# for i in range(num_rectangles):
#     color = input(f"\nВведите цвет {i+1}-го прямоугольника: ")
#     rect = Rectangle(color)
#     rect.input_dimensions()
#     rectangles.append(rect)
#
# # Вызовы
# for rect in rectangles:
#     # rect.calculate_area()
#     rect.calculate_area_rectangle(rect.length, rect.width)







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
# print(hello.__name__)  # Вывод: hello
# print(hello.__doc__)   # Вывод: Приветствует пользователя
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
#
# # Ввод и вызов в две строки
# width, height = map(int, input().split())
# get_sq = func_show(get_sq)
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


"""Пример"""

# def decorator_func(func):
#     def wrapper_func(a, b):
#         result = func(a, b)
#         print('До декорируемой функции')
#         print('Результат = ', result)
#         print('После декорируемой функции')
#         return result
#     return wrapper_func
#
# @decorator_func
# def calculate_area_rectangle(length, width):
#     return length * width
#
# user_input_length = int(input('Введите длину: '))
# user_input_width = int(input('Введите ширину: '))
#
# calculate_area_rectangle(user_input_length, user_input_width)














