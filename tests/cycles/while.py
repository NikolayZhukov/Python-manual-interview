
names = input().split()

i = 0
while i < len(names):
    if names[i][0].lower() == names[i][-1].lower():
        print('ДА')
        break
    i += 1
else:
    print("НЕТ")

# # Читаем строку и формируем список городов
# cities = input().split()
#
# i = 0
# while i < len(cities):
#     if len(cities[i]) <= 5:   # если длина города 5 или меньше
#         print("НЕТ")
#         break
#     i += 1
# else:
#     # Цикл завершился без break
#     print("ДА")




# i = 1
# while i <= 10:
#     if i % 2 == 1:
#         print(i, end=' ')
#     i += 1



# i = 100                 # начинаем с первого трёхзначного числа
# while i <= 999:         # пока не превысили диапазон
#     if i % 47 == 43 and i % 3 == 0:
#         print(i, end=' ')
#     i += 1


# n, m = map(int, input().split())
# # если n чётное – начинаем со следующего числа, чтобы старт был нечётным
# n += n % 2 == 0   # булево True/False преобразуется в 1/0
# while n <= m:
#     print(n, end=' ')
#     n += 2



# years = int(input())
# start_year = 0
# current_capital = 1000
#
# while start_year < years:
#     current_capital += current_capital / 100 * 5
#
#     start_year += 1
# print(round(current_capital, 2))

# n = int(input())
# times = round(n // 3)
# c = 1
# sum = 1
#
# while c <= times:
#     sum *= 2
#     c += 1
# print(sum)



"""Фибоначчи"""
# n = int(input())   # читаем целое число n (n >= 2)
#
# a, b = 1, 1        # первые два числа Фибоначчи
# count = 2          # уже есть два числа
# print(a, b, end=' ')   # выводим первые два числа
#
# while count < n:        # пока не выведем n чисел
#     a, b = b, a + b     # сдвигаем: новое число = сумма двух предыдущих
#     print(b, end=' ')
#     count += 1



# a = list(map(int, input()))
# sum = a[0]
# n = 0
#
# while n < len(a) - 1:
#     sum *= a[n + 1]
#     n += 1
# print(sum)


# frase = input()
#
# while "--" in frase:
#     frase = frase.replace("--", "-")
# print(frase)


# a = None
# sum = 0
#
# while a != 0:
#     a = int(input())
#     sum += a
# print(sum)


# n = int(input())
# a = 1
# s = 0
#
# while a <= n:
#     s += 1/a
#     a += 1
# print(round(s, 3))


#
# price = float(input())
# number_books = 2
# list_prices = []
#
# while 10 >= number_books >= 2:
#     final_price = (price * number_books)
#     list_prices.append(round(final_price, 1))
#     number_books += 1
# print(*list_prices)



# n, m = map(int, input().split())
# i = n
# result = []
#
# while n <= i <= m:
#     value = (i ** 2)
#     result.append(value)
#     i += 1
# print(*result)

