# список нот
m = ['до', 'ре', 'ми', 'фа', 'соль', 'ля', 'си']

# считываем три целых числа
nums = list(map(int, input().split()))

# формируем список названий с условием на диез
result = [(('#' + m[n-1]) if m[n-1] in ('до', 'фа') else m[n-1]) for n in nums]

# выводим строку
print(' '.join(result))




# a = int(input())
# min_num = 0
# max_num = 59
# next_num = a + 1 if 0 <= a < 59 else 0
# print(next_num)


# a = int(input())
# b = "False" if a == 0 else "True"
# print(b)


# word = input()
# msg = "палиндром" if word[0]+word[1] == word[-1]+word[-2] else "не палиндром"
# print(msg)

# word = (input()).lower()
# msg = "палиндром" if word[0] == word[-1] and word[1] == word[-2] else "не палиндром"
# print(msg)


# a = int(input())
#
# msg = 'кратно 3' if a % 3 == 0 else 'не кратно 3'
# print(msg)

# a = float(input())
# b = float(input())
#
# d = a if a > b else b
# print(d)


# '''ТЕРНАРНЫЙ ОПЕРАТОР'''
#
# a = 2
# b = 7
#
# res = a if a > b else b
# print(res)

# k = int(input())  # 1 <= k <= 365
#
# days = ["понедельник", "вторник", "среда",
#         "четверг", "пятница", "суббота", "воскресенье"]
#
# # (k-1) % 7 — смещение от понедельника
# print(days[(k - 1) % 7])



# m, n = map(int, input().split())
#
# days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#
# # --- проверки исходной даты ---
# if m == 1 and n == 1:
#     print("Ошибка: дата не может быть 1 января")
#     exit()
# if m == 12 and n == 31:
#     print("Ошибка: дата не может быть 31 декабря")
#     exit()
#
# # --- предыдущий день ---
# if n > 1:
#     prev_m, prev_d = m, n - 1
# else:                               # первый день месяца
#     prev_m = m - 1
#     prev_d = days_in_month[prev_m - 1]
#
# # --- следующий день ---
# if n < days_in_month[m - 1]:
#     next_m, next_d = m, n + 1
# else:                               # последний день месяца
#     next_m = m + 1
#     next_d = 1
# print(f"{prev_m:02d}.{prev_d:02d} {next_m:02d}.{next_d:02d}")





# month = int(input())
# thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
# thirty_days = [4, 6, 9, 11]
# twenty_eight_days = [2]
#
# if month in thirty_one_days:
#     print('31')
# elif month in thirty_days:
#     print('30')
# elif month in twenty_eight_days:
#     print('28')


# number = int(input())
# if number == 1:
#     print('понедельник')
# elif number == 2:
#     print('вторник')
# elif number == 3:
#     print('среда')
# elif number == 4:
#     print('четверг')
# elif number == 5:
#     print('пятница')
# elif number == 6:
#     print('суббота')
# elif number == 7:
#     print('воскресенье')


# number = float(input())
# if number <= 60:
#     print(1)
# elif 60 < number <=64:
#     print(2)
# elif 64 < number <= 69:
#     print(3)
# elif 69 < number:
#     print(4)


# numbers = list(map(int, input().split()))
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
#
# if a <= b and a <= c:
#     print(a)
# elif b <= a and b <= c:
#     print(b)
# else:
#     print(c)




# m = ['1. Введение в Python',
# '2. Строки и списки',
# '3. Условные операторы',
# '4. Циклы',
# '5. Словари, кортежи и множества',
# '6. Выход']
#
# number = int(input())
# number = str(number)
#
# if number in m[0]:
#     print(m[0])
# elif number in m[1]:
#     print(m[1])
# elif number in m[2]:
#     print(m[2])
# elif number in m[3]:
#     print(m[3])
# elif number in m[4]:
#     print(m[4])
# elif number in m[5]:
#     print(m[5])


# t = float(input())
# position_time = t % 5
# if position_time > 3:
#     print('red')
# else:
#     print('green')


# number = list(map(int, input()))
# if number[0] + number[1] + number[2] == number[3] + number[4] + number[5]:
#     print('ДА')
# else:
#     print('НЕТ')

# numbers = list(map(int, input().split()))
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# d = numbers[3]
#
# a_min = a - 2
# b_min = b - 2
#
# if (a_min >= c and b_min >= d) or (a_min >= d and b_min >= c):
#     print('ДА')
# else:
#     print('НЕТ')


# cities = input().split()
# if 'Москва' in cities:
#     cities.remove('Москва')
# print(*cities)

# word = input()
# if 't' in word and 'h' in word and 'o' in word:
#     print('ДА')
# else:
#     print('НЕТ')


# numbers = str(int(input()))
# if numbers[-1] == '7':
#     print('ДА')
# else:
#     print('НЕТ')

# numbers = list(map(int, input().split()))
# a = numbers[0]
# b = numbers[1]
# c = numbers[2]
# if (a ** 2) + (b ** 2) == c ** 2:
#     print('ДА')
# else:
#     print('НЕТ')




# write = list(map(int, input().split()))
# m = write[0]
# n = write[1]
# if m % n == 0:
#     print(int(m / n))
# else:
#     print(f'{m} на {n} нацело не делится')



# word1 = input()
# word1 = word1.lower()
# if word1[0] != word1[-1]:
#     print('НЕТ')
# elif word1[1] != word1[-2]:
#     print('НЕТ')
# else:
#     print('ДА')


# n1 = list(map(float, input().split()))
# if n1[0] > n1[1]:
#     print(n1[0])
# else:
#     print(n1[1])


# x = 1
# if True:
#     print(x)