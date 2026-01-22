class Person:
    def __init__(self, name):
        self.name = name

Alex = Person('Alex')

print(Alex.__dict__)     # {'name': 'Alex'} - атрибуты экземпляра
# print(Alex.__class__)    # <class '__main__.Person'> - класс объекта
# print(Alex.__module__)   # '__main__' - модуль, где объявлен класс
# print(Person.__name__)   # 'Person' - имя класса
# print(Person.__bases__)  # (<class 'object'>,) - родительские классы