# class Person:
#     def __init__(self, name):
#         self.name = name
#
# p = Person("Alice")
#
# print(repr(p))       # <__main__.Person object at 0x7f...>
# print(p.__repr__())


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # def __str__(self):
    #     return f'{self.name}, {self.age} years old'

    def __repr__(self):
        return f'{self.name}, {self.age} years old'

person = Person('Alice', 30)
print(repr(person))
print(person.name)


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# person = Person('Alice', 30)
# print(repr(person))
# # print(repr(person.name))




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