def even(y):
    return y % 2 == 0   # True, если чётное; False, если нечётное

# запускаем цикл ввода
while True:
    x = int(input())    # читаем число
    if x == 1:          # условие выхода
        break
    if even(x):         # проверка через функцию
        print(x)

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

