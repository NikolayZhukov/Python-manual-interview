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

# Меняем один элемент списка
my_list[2] = "д"  # Заменяем "т" на "д"
print(f"Измененный список: {my_list}")
print(f"ID списка после изменения: {id(my_list)}")
print(f"ID элементов списка после изменения: {[id(item) for item in my_list]}")
print()

# Проверяем, изменился ли id списка
print(f"ID списка остался прежним: {id(my_list) == id(my_list)}")


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