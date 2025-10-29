""" """




"""Как возвести в степень каждое значение всех вложенных списков и сохранить структуру вложенности
a = [[4,2,3,3], [1,3,5,8], [4,9,8,5]] ? """

# """1-е решение"""
# a = [[4,2,3,3], [1,3,5,8], [4,9,8,5]]
# b = []
# b = [[x ** 2 for x in lst] for lst in a]
# print(b)
#
# """2-е решение"""
# a = [[4,2,3,3], [1,3,5,8], [4,9,8,5]]
# b = []
# for lst in a:
#     temp = []
#     for x in lst:
#       temp.append(x ** 2)
#     b.append(temp)
# print(b)



#
#
a = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
for lst in a:
    for x in lst:
        print(x**2, end=' ')
    print()
#
#
#
# a = [[4,2,3,3], [1,3,5,8], [4,9,8,5]]
# b = [[5,2,5,3], [5,3,5,4], [6,9,1,1]]
# c = []
# for i in range(len(a)):
#     r = []
#     for j in range(len(a[i])):
#         r.append(a[i][j] + b[i][j])
#     c.append(r)
# print(c)
#
#
# numbers = list(map(float, input().split()))
#
# for i, d in enumerate(numbers):
#     if d < 0:
#         numbers[i] = -1.0
#
# print(*numbers)
#
#
# numbers = list(map(float, input().split()))
# if numbers:
#     min_number = numbers[0]
#     for num in numbers[1:]:
#         if num < min_number:
#             min_number = num
#     numbers = min_number
#     print(numbers)
# else:
#     print("Список пуст")
#
#
# numbers = list(map(float, input().split()))
# if numbers:
#     min_number = numbers[0]
#     for num in numbers[1:]:
#         if num < min_number:
#             min_number = num
#     print(min_number)
# else:
#     print("Список пуст")
#
#
# numbers = list(input().split())
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] + ' ' + numbers[i]
# print(*numbers)
#
#
# numbers = input().split()
#
# for i in range(len(numbers)):
#     numbers[i] = numbers[i] * 2  # numbers[i] уже строка!
#
# print(''.join(numbers))
#
# numbers = input().split()  # ['2', '3', '4']
# number = int(''.join(numbers))  # '234' -> 234
# print(number)
#
#
# numbers = list(map(int, input().split()))
# for i, d in enumerate(numbers):
#     numbers[i] = abs(d) ** 2
# print(*numbers)
#
#

# """1-е решение"""
# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# for i, d in enumerate(digs):
#     if 10 <= abs(d) <= 99:
#         digs[i] = 0
#
# print(digs)
#
# """2-е решение"""
# digs = [4, 3, 100, -53, -30, 1, 34, -8]
#
# for i in range(len(digs)):
#     if 10 <= abs(digs[i]) <= 99:
#         digs[i] = 0
#
# print(digs)
#
#
# words = ['Python', 'дай', 'мне', 'силы']
# frase = (' '.join(words))
# print(frase)
#
#
# n = int(input("Введите число от 1 до 100: "))
# sum = 1
# if 1 > n > 100:
#     n = int(input("Введите число от 1 до 100: "))
# else:
#     for i in range(1, n+1):
#         sum *= i
#     print(sum)
#
#
#
# for i in range(1, 6):
#     print('*' * i)
#
#
# n = int(input())
# sum = 0
#
# for i in range(n):
#     if i % 3 == 0 or i % 5 == 0:
#         sum += i
# print(sum)
#
#
#
# cities = input().split()
#
# for i in range(len(cities)):
#     cities[i]=len(cities[i])
#     print(cities[i], end=' ')
#
#
# n = list(map(int, input().split()))
# sum = 0
# for i in n:
#     sum += i if i % 2 == 1 else 0
# print(sum)
#
#
#
# for i in range(1, 20, 3):
#     print(i, end=' ')
#
#
#
# for x in range(-10, -1):
#     if x % 2 == 0:
#         print(x, end=' ')
#
#
# for x in range(11):
#     print(x, end=' ')
#
# for x in range(-10, 1):
#     print(x, end=' ')