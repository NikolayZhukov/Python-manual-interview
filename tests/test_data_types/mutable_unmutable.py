"""Что такое изменяемые типы данных? Что означает конкретно?
Изменяемые (mutable) типы данных в Python — это типы,
объекты которых можно изменить после их создания,
при этом id объекта (его идентификатор в памяти) остается прежним.
"""

my_list = ["к", "о", "т"]
print(f"Исходный список: {my_list}")
print(f"ID списка: {id(my_list)}")
print(f"ID элементов списка: {[id(item) for item in my_list]}")
print()
#
# # Меняем один элемент списка
# my_list[2] = "д"  # Заменяем "т" на "д"
# print(f"Измененный список: {my_list}")
# print(f"ID списка после изменения: {id(my_list)}")
# print(f"ID элементов списка после изменения: {[id(item) for item in my_list]}")
# print()
#
# new_list1 = my_list + ['Чёрный1']
# print(f'my_list - {my_list}')
# print(f'new_list1 - {new_list1}')
#
# new_list2 = my_list.copy()
# new_list2.append('Чёрный2')
# print(f'my_list - {my_list}')
# print(f'new_list2 - {new_list2}')
#
#
# # Проверяем, изменился ли id списка
# print(f"ID списка остался прежним: {id(my_list) == id(my_list)}")



"""Как проявляется изменяемость типа данных при работе с функциями?"""

# def add_element_bad(lst, element):
#     """Функция изменяет переданный список"""
#     lst.append(element)
#     return lst
#
# my_list = [1, 2, 3]
# print(f"До функции: {my_list}, id: {id(my_list)}")
#
# result = add_element_bad(my_list, 4)
# print(f"После функции: {my_list}")  # Исходный список изменился!
# print(f"Результат: {result}")
# print(f"ID исходного списка: {id(my_list)}")
# print(f"ID результата: {id(result)}")
# print(f"Это один и тот же объект: {my_list is result}")


# def add_element_good(lst, element):
#     """Функция не изменяет переданный список"""
#     new_lst = lst.copy()  # Создаем копию
#     new_lst.append(element)
#     return new_lst
#
# my_list = [1, 2, 3]
# print(f"До функции: {my_list}, id: {id(my_list)}")
#
# result = add_element_good(my_list, 4)
# print(f"После функции: {my_list}")  # Исходный список не изменился!
# print(f"Результат: {result}")
# print(f"ID исходного списка: {id(my_list)}")
# print(f"ID результата: {id(result)}")
# print(f"Это один и тот же объект: {my_list is result}")


# #неизменяемые
# int_obj = 12345
# print("id of int_obj: ", id(int_obj))
# print("id of int_obj: ", id(int_obj))

# #изменяемые
# list_obj = [10, 20, 30]
# print("id of list_obj: ", id(list_obj))
# print("id of list_obj: ", id(list_obj))



# #неизменяемые
# int_obj = 10
# print("id of int_obj: ", id(int_obj))
# int_obj += 5
# print("id of int_obj: ", id(int_obj))
#
#
# #изменяемые
# list_obj = [10, 20, 30]
# print("id of list_obj: ", id(list_obj))
#
# list_obj += [40]
# print("id of list_obj: ", id(list_obj))

# Исходная строка
# my_string = "кот"
# print(f"Исходная строка: '{my_string}'")
# print(f"ID исходной строки: {id(my_string)}")
# print()
#
# # Пытаемся "добавить" символ в конец
# new_string = my_string + "!"  # Создается НОВАЯ строка
# print(f"Новая строка: '{new_string}'")
# print(f"ID новой строки: {id(new_string)}")
# print()
#
# # Сравниваем объекты
# print(f"Исходная строка осталась неизменной: '{my_string}'")
# print(f"ID исходной строки не изменился: {id(my_string)}")
# print(f"Это разные объекты: {my_string is new_string}")
# print()
#
# # Еще один пример с конкатенацией
# another_string = my_string + "ёнок"
# print(f"Еще одна новая строка: '{another_string}'")
# print(f"ID еще одной новой строки: {id(another_string)}")