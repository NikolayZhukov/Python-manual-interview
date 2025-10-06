
def calculate_age(birth_year):
    if birth_year > 2024:
        raise ValueError("Год рождения не может быть в будущем")
    if birth_year < 1900:
        raise ValueError("Слишком старый год рождения")

    return 2024 - birth_year

# Использование
try:
    age = calculate_age(2001) # Вызовет исключение
    print(f'Ваш возраст - {age}')
except ValueError as e:
    print(f"Ошибка: {e}")


# print(calculate_age(1957))


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


# try:
#     f = open("data.txt", "r")
#     content = f.read()
# except FileNotFoundError:
#     print("Файл не найден")
# except PermissionError:
#     print("Нет доступа к файлу")
# except:
#     print('Произошла ошибка')



# try:
#     x = int("2d2")   # вызовет ValueError
# except ValueError:
#     print("Неверное преобразование строки в число")
# else:
#     print("Преобразование прошло успешно", x)
# finally:
#     print("Закрываю ресурс")