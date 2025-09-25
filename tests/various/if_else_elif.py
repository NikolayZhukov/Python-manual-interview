

numbers = list(map(int, input().split()))
a = numbers[0]
b = numbers[1]
c = numbers[2]

if a <= b and a <= c:
    print(a)
elif b <= a and b <= c:
    print(b)
else:
    print(c)




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