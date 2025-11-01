# class Calculator:
#     @staticmethod
#     def add(a, b):
#         return a + b
#
#     @staticmethod
#     def multiply(a, b):
#         return a * b
#
# # Использование без создания экземпляра
# result1 = Calculator.add(5, 5)  # 8
# result2 = Calculator.multiply(4, 2)  # 8
#
# print(result1, result2)


# class Animal:
#     pass
#
# class Dog(Animal):
#     pass
#
# class Cat(Animal):
#     pass
#
# # Создаем объекты
# my_dog = Dog()
# my_cat = Cat()
#
# print(isinstance(my_dog, Dog))





# class User:
#     # protected - доступен только в классе или же те дочерним классам
#     _emp_name = None
#     _age = None
#
#     # private - доступен только в самом классе
#     __branch = None
#
#     # конструктор
#     def __init__(self, emp_name, age, branch):
#         self._emp_name = emp_name
#         self._age = age
#         self.__branch = branch
#
#     # публичный метод - общедоступный метод
#     def display(self):
#         print(self._emp_name + " " + self._age + " " + self.__branch)



# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, vector):
#         return Vector(self.x + vector.x, self.y + vector.y)
#
#     def __sub__(self, vector):
#         return Vector(self.x - vector.x, self.y - vector.y)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
#
# print(v1 + v2)  # Вывод: Vector(4, 6)
# print(v1 - v2)  # Вывод: Vector(-2, -2)




# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, vector):
#         return Vector(self.x + vector.x, self.y + vector.y)
#
#     def __sub__(self, vector):
#         return Vector(self.x - vector.x, self.y - vector.y)
#
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"
#
#
# v1 = Vector(1, 2)
# v2 = Vector(3, 4)
#
# print(v1 + v2)  # Вывод: Vector(4, 6)
# print(v1 - v2)  # Вывод: Vector(-2, -2)




# import copy
#
# original1 = [1, 2, [3, 4]]
# shallow_copy = original1.copy()
# print(shallow_copy)
# print(id(shallow_copy))
# print(id(original1))
#
# original2 = [1, 2, [3, 4]]
# deep_copy = copy.deepcopy(original2)
# print(deep_copy)
# print(id(deep_copy))
# print(id(original2))



# def myEmptyFunc():
#     pass
#
# myEmptyFunc()