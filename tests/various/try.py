

# def division():
#     try:
#         a, b = map(int, input().split())
#         c = a / b
#     except ValueError:
#         print('Введите именно число, а не букву!')
#     except ZeroDivisionError:
#         print('Введите любое число кроме ноля! На ноль делить нельзя!')
#     else:
#         return c
#     finally:
#         print('Ждём вас снова!')
#
# division()


try:
    f = open("data.txt", "r")
    content = f.read()
except FileNotFoundError:
    print("Файл не найден")
except PermissionError:
    print("Нет доступа к файлу")
except:
    print('Произошла ошибка')



# try:
#     x = int("2d2")   # вызовет ValueError
# except ValueError:
#     print("Неверное преобразование строки в число")
# else:
#     print("Преобразование прошло успешно", x)
# finally:
#     print("Закрываю ресурс")