


# a = (i*i for i in range(5))
#
# print("Первый проход:")
# for i in a:
#     print(i)  # Выведет 0, 1, 4, 9, 16
#
# print("Второй проход:")
# for i in a:
#     print(i)  # НИЧЕГО не выведет! Генератор уже исчерпан

# print("ab" in "abra")

# print("A" < "a")
# print(ord("A"))
# print(ord("a"))

# a = [5]
# b = [5]
# print(id(a))
# print(id(b))
#
# a = (5555.1,)
# b = '5555'
# print(id(a))
# print(id(b))
#
# print(type(a))
# print(type(b))
#
# c = 7 // 2
# print(c)
#
# d = -7 // 2
# print(d)
#
# e = 10 % 3
# print(e)
#
# i = 3
# i += 1
# print(i)
#
# f = 3
# f -= 1
# print(f)
#
# g = 3
# g *= 3
# print(g)
#
# h = 3
# h /= 3
# print(h)
#
#
# x = 10  # глобальная переменная
#
# def change_x():
#     global x      # говорим, что будем использовать глобальную переменную x
#     x = 20        # изменяем глобальную x
#
# print("До вызова функции:", x)  # 10
# change_x()
# print("После вызова функции:", x)  # 20
#
#
# def outer():
#     x = 10  # переменная во внешней функции
#
#     def inner():
#         nonlocal x   # используем x из outer(), а не создаём новую локальную
#         x = 20       # изменяем x из внешней функции
#
#     inner()
#     print("Значение x во внешней функции:", x)
#
# outer()