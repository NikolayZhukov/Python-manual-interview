""""""
"""
1. метод get
Возвращает значение по ключу
"""
# person = {'name': 'Alice', 'age': 25, 'city': 'Moscow'}
#
# print(person.get('name'))
# print(person.get('age'))
# print(person.get('country'))
# print(person.get('country', 'Не указано'))


"""
2. setdefault()
Если ключ есть — возвращает значение
# """
# person = {'name': 'Alice', 'age': 25}
#
# print(person.setdefault('name', 'Unknown'))
# print(person.setdefault('country', 'Unknown'))

"""
3. keys
Получить все ключи
"""

# person = {'name': 'Alice', 'age': 25, 'city': 'Moscow'}

# keys = person.keys()
# print(keys)
# print(list(keys))

# & - общие ключи для двух словарей
# person2 = {'name': 'Bob', 'country': 'Russia'}
# common = person.keys() & person2.keys()
# print(common)


"""
4. values
"""
# person = {'name': 'Alice', 'age': 25, 'city': 'Moscow'}
#
# values = person.values()
# print(values)         # dict_values(['Alice', 25, 'Moscow'])
# print(list(values))   # ['Alice', 25, 'Moscow']
#
# # Поиск по значению (медленно для больших словарей)
# if 25 in person.values():
#     print("Есть возраст 25")


"""
5. items()
"""

person = {'name': 'Alice', 'age': 25, 'city': 'Moscow'}

items = person.items()
# print(items)  # dict_items([('name', 'Alice'), ('age', 25), ('city', 'Moscow')])

# Итерация по словарю
# for key, value in person.items():
#     print(f"{key}: {value}")

# Преобразование в список кортежей
# a = list(items)
# print(a)


"""
6. dict.fromkeys() — создание из списка словаря с ключам и значениями по умолчанию
"""
# Создание словаря из списка ключей
# keys = ['name', 'age', 'city']
# default_dict = dict.fromkeys(keys)
# print(default_dict)  # {'name': None, 'age': None, 'city': None}

# С общим значением
# default_dict = dict.fromkeys(keys, 'Не указано')
# print(default_dict)  # {'name': 'Не указано', 'age': 'Не указано', 'city': 'Не указано'}
