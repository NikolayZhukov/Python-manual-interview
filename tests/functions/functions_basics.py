digs = list(map(int, input().split()))
a1 = max(digs)
b1 = min(digs)

def multiply(a, b):
    sum = a * b
    return sum

print(multiply(a1, b1))


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

