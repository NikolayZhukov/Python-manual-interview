""""""

"""
Напишите программу, которая постоянно запрашивает у пользователя ввод чисел. 
Процесс останавливается, когда пользователь вводит слово "стоп". 
После этого программа выводит сумму всех введенных чисел.
"""
# total = 0
#
# while True:
#     user_input = input("Введите число (или 'стоп' для выхода): ")
#
#     if user_input.lower() == "стоп":
#         break  # Выход из цикла
#
#     # Пытаемся преобразовать ввод в число
#     try:
#         number = float(user_input)
#         total += number
#     except ValueError:
#         print("Это не число! Попробуйте снова.")
#
# print(f"Сумма всех введенных чисел: {total}")


"""
Программа загадывает случайное число от 1 до 10. 
Пользователь должен угадать его. 
На каждой попытке программа подсказывает, больше или меньше названное число загаданного. 
Цикл продолжается, пока число не будет угадано. 
В конце выводится количество попыток.
Здесь цикл while работает до тех пор, пока условие guess != secret_number является истиной. 
Внутри цикла мы меняем переменную attempts, чтобы вести счет.
"""
import random

secret_number = int(input('Введите секретное число от 1 до 10: '))
attempts = 0
guess = None

print("Я загадал число от 1 до 10. Попробуй угадать!")

while guess != secret_number:
    try:
        guess = int(input("Твоя догадка: "))
        attempts += 1

        if guess < secret_number:
            print("Мое число больше.")
        elif guess > secret_number:  # заменил if на elif
            print("Мое число меньше.")
        else:
            print(f"Поздравляю! Ты угадал с {attempts}-й попытки!")
            break  # добавляем break для остановки игры

    except ValueError:
        print("Пожалуйста, вводи только целые числа!")






"""
С помощью цикла while напишите программу, которая выводит все нечетные числа от 1 до 10 включительно. Все числа должны быть выведены в одну строку через пробел.
"""
# i = 1
# while i <= 10:
#     if i % 2 == 1:
#         print(i, end=' ')
#     i += 1


"""
С помощью цикла while напишите программу, которая выводит все нечетные числа от 1 до 10 включительно. Все числа должны быть выведены в одну строку через пробел.
"""
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i, end=' ')
#     i += 1



"""
С помощью цикла while напишите программу, которая выведет все числа от 0 до 1000, 
которые делятся без остатка на 47 и на 3.
"""
# i = 100
# while i <= 999:
#     if i % 47 == 0 and i % 3 == 0:
#         print(i, end=' ')
#     i += 1


"""
Выведите последовательность чисел Фибоначчи в диапазоне от 1 до 100:

"""
# a = 1
# b = 1
# print(a, end=' ')
#
# while b <= 100:
#     print(b, end=' ')
#     a, b = b, a + b


# a = 1
# b = 1
# print(a, end=' ')
#
# while b <= 100:
#     print(b, end=' ')
#     old_a = a
#     a = b
#     b = old_a + b


"""
Напишите программу, которая принимает два целых числа N и M (где N ≤ M) и выводит квадраты всех целых чисел от N до M включительно.
Числа выводятся в одну строку через пробел.
"""
# n, m = map(int, input().split())
# i = n
# result = []
#
# while n <= i <= m:
#     value = (i ** 2)
#     result.append(value)
#     i += 1
# print(*result)
























# names = input().split()
#
# i = 0
# while i < len(names):
#     if names[i][0].lower() == names[i][-1].lower():
#         print('ДА')
#         break
#     i += 1
# else:
#     print("НЕТ")

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

#
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




