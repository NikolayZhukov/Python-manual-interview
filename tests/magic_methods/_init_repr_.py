""""""
"""Как напечатать все атрибуты экземплаяра класса?
1. С помощью магических методов
   1.1. __repr__ 
   1.2. __str__
   1.3. __dict__
2. Без магических методов
   2.1. Обращаться напрямую к атрибуту
   2.2. Создать отдельный метод для печати
   2.3. Использовать vars() для получения всех атрибутов 
"""

"""
1. С помощью магических методов
   1.1. __repr__ 
   1.2. __str__
"""
#
# class Person():
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#
#     def __repr__(self):
#         # Техническая информация - можно скопировать и создать объект
#         return f"Person('{self.name}', {self.age}, '{self.nationality}')"
#
#     def __str__(self):
#         # Красивое отображение для пользователя
#         return f"Человек: {self.name}, {self.age} лет, из {self.nationality}"
#
# Alex = Person('Alex', 19, 'Бразилии')
#
# print(repr(Alex))  # Person('Alex', 19, 'Бразилии')
# print(str(Alex))   # Человек: Alex, 19 лет, из Бразилии
# print(Alex)        # Человек: Alex, 19 лет, из Бразилии (автоматически str)


"""1.3. __dict__"""

class Person():
    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality

Alex = Person('Alex', 19, 'brasilian')
print(Alex.__dict__)
# Вывод: {'name': 'Alex', 'age': 19, 'nationality': 'brasilian'}



"""
2. Без магических методов
   2.1. Обращаться напрямую к атрибуту
"""

# class Person():
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#
# Alex = Person('Alex', 19, 'brasilian')
# print(f"Имя: {Alex.name}, Возраст: {Alex.age}, Национальность: {Alex.nationality}")
# # Вывод: Имя: Alex, Возраст: 19, Национальность: brasilian


"""
2.2. Создать отдельный метод для печати
"""

# class Person():
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#
#     def print_info(self):
#         print(f"Имя: {self.name}, Возраст: {self.age}, Национальность: {self.nationality}")
#
#
# Alex = Person('Alex', 19, 'brasilian')
# Alex.print_info()
# # Вывод: Имя: Alex, Возраст: 19, Национальность: brasilian


"""
2.3. Использовать vars() для получения всех атрибутов 
"""
# class Person():
#     def __init__(self, name, age, nationality):
#         self.name = name
#         self.age = age
#         self.nationality = nationality
#
# Alex = Person('Alex', 19, 'brasilian')
# print(vars(Alex))
# # Вывод: {'name': 'Alex', 'age': 19, 'nationality': 'brasilian'}




# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person("Alice")
#
# print(repr(p))       # <__main__.Person object at 0x7f...>
# print(p.__repr__())


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     # def __str__(self):
#     #     return f'{self.name}, {self.age} years old'
#
#     def __repr__(self):
#         return f'{self.name}, {self.age} years old'
#
# person = Person('Alice', 30)
# print(repr(person))
# print(person.name)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person = Person('Alice', 30)
# print(repr(person))
# print(repr(person.name))




# @pytest.fixture
# def test_data():
#     """Фикстура для генерации уникальных данных для каждого теста"""
#     return {
#         'unique_name': generate_random_string(),
#         'unique_name_new': generate_random_string()
# }
#
# class MainPage(MdmPage):
#     def __init__(self, page: Page, test_data: dict):
#         super().__init__(page)
#         self.test_data = test_data


