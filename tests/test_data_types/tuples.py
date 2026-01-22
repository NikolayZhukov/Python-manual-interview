""""""
"""
Распаковка кортежей в цикле
"""

# students = [
#     ("Алексей", 20, "информатика"),
#     ("Мария", 19, "физика"),
#     ("Иван", 21, "математика")
# ]
#
# for name, age, specialty in students:
#     print(f"Имя: {name}, Возраст: {age}, Специальность: {specialty}")




"""
1) Используя распаковку в цикле, вычислите средний балл каждого студента
students_grades = [
#     ("Алексей", "математика", 85, 92, 78),
#     ("Мария", "физика", 90, 88, 95),
#     ("Иван", "информатика", 76, 85, 80),
#     ("Елена", "математика", 92, 96, 89),
#     ("Дмитрий", "физика", 82, 79, 85)
# ]
"""

"""1 способ"""
# students_grades = [
#     ("Алексей", "математика", 85, 92, 78),
#     ("Мария", "физика", 90, 88, 95),
#     ("Иван", "информатика", 76, 85, 80),
#     ("Елена", "математика", 92, 96, 89),
#     ("Дмитрий", "физика", 82, 79, 85)
# ]
# print("Средние баллы студентов:")
# for name, subject, *grades in students_grades:
#     avg_grade = sum(grades) / len(grades)
#     print(f"{name} ({subject}): {avg_grade:.1f}")

"""2 способ"""
# students_grades = [
#     ("Алексей", "математика", 85, 92, 78),
#     ("Мария", "физика", 90, 88, 95),
#     ("Иван", "информатика", 76, 85, 80),
#     ("Елена", "математика", 92, 96, 89),
#     ("Дмитрий", "физика", 82, 79, 85)
# ]
#
#
# for name, subject, point1, point2, point3 in students_grades:
#     medium = (point1 + point2 + point3) / 3
#     print(f'Имя: {name}\nПредмет: {subject}\nСредний балл: {medium}')
#     print("-" * 20)

"""
2) Отсортируйте студентов по среднему баллу (по убыванию)
# students_grades = [
#     ("Алексей", "математика", 85, 92, 78),
#     ("Мария", "физика", 90, 88, 95),
#     ("Иван", "информатика", 76, 85, 80),
#     ("Елена", "математика", 92, 96, 89),
#     ("Дмитрий", "физика", 82, 79, 85)
# ]
"""
students_grades = [
    ("Алексей", "математика", 85, 92, 78),
    ("Мария", "физика", 90, 88, 95),
    ("Иван", "информатика", 76, 85, 80),
    ("Елена", "математика", 92, 96, 89),
    ("Дмитрий", "физика", 82, 79, 85)
]
# print("\nРейтинг студентов по среднему баллу:")
# student_ratings = []
# for name, subject, *grades in students_grades:
#     avg_grade = sum(grades) / len(grades)
#     student_ratings.append((name, subject, avg_grade))
#
# sorted_students = sorted(student_ratings, key=lambda x: x[2], reverse=True)
#
# for name, subject, avg in sorted_students:
#     print(f"{name}: {avg:.1f} баллов ({subject})")


# names = tuple(input().split())
# names_list = list(names)
# names_list = [name.lower() for name in names_list]
# names_list_in = [name for name in names_list if 'ва' in name]
# print(*names_list_in)




# cities = tuple(input().split())
# cities = list(cities)
# city = 'Ульяновск'
# if city in cities:
#     cities.remove(city)
# print(*cities)


# cities = (input().split())
# city = 'Москва'
# cities.append(city) if city not in cities else cities
# cities = tuple(cities)
# print(*cities)





# t = (3.4, -56.7)
# a = list(map(int, input().split()))
# t_lst = list(t) + a
# t = tuple(t_lst)
# print(t)




# a, b = (1, 2)
# print(a)


# a = tuple('hello, world!')
# print(a)
# print(id(a))


# a = tuple('hello, world!')
# print(type(a))
# for i in a:
#     print(i)

# a = (1,3,7)
# print(type(a))
# for i in a:
#     print(i)
