""""""

"""Магические методы"""
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __str__(self):
#         return f"Point({self.x}, {self.y})"
#
#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1)          # вызывает __str__ → "Point(1, 2)"
# print(p1 + p2)     # вызывает __add__ → Point(4, 6)


"""То же самое, но без магических методов"""
# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     # Обычный метод для текстового представления
#     def to_string(self):
#         return f"Point({self.x}, {self.y})"
#
#     # Обычный метод для сложения точек
#     def add(self, other):
#         return Point(self.x + other.x, self.y + other.y)
#
# p1 = Point(1, 2)
# p2 = Point(3, 4)
#
# # Вызываем свои методы напрямую
# print(p1.to_string())      # "Point(1, 2)"
# p3 = p1.add(p2)
# print(p3.to_string())      # "Point(4, 6)"
