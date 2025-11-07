""" """

"""
Напиши программу, которая будет складывать соответствующие пары из двух списков и сохранять в третий список
"""
# lst1 = [4,9,8,5]
# lst2 = [6,9,1,1]
# list_sum = [lst1[i] + lst2[i] for i in range(len(lst1))]
# print(*list_sum)



"""
Дан список целых чисел. Напишите программу, которая выводит все элементы, 
находящиеся на четных позициях (с четными индексами) в исходном списке.
"""

# numbers = [4, 5, 7, 12, 56]
# result = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
# print(*result)

"""
С помощью enumerate
"""
# numbers = [4, 5, 7, 12, 56]
# result = []
# for i, num in enumerate(numbers):
#     if i % 2 == 0:
#         result.append(num)
# print(*result)


"""
Выведите список с городами, в которых меньше 9 букв.
"""
# cities = ["Mosca", "Londra", "Napoli", "Sanpietroburgo", "Amsterdam", "Manchester"]
#
# cities_selected = [i for i in cities if len(i) < 9]
# print(cities_selected)


"""
Выведите список квадратов чисел, от ноля до числа n, получаемое через ввод пользователем.
"""
# n = int(input())
# sum = [x ** 2 for x in range(n)]
# print(sum)











# lst1 = input().split()
# lst2 = [[lst1[i], int(lst1[i+1])] for i in range(0, len(lst1), 2)]
# print(lst2)



# lst = list(map(float, input().split()))
# list_2 = [lst[i] for i in range(len(lst))
#           if i % 2 == 0
#           ]
# print(*list_2)


# lst = list(map(int, input()))
# print(lst)

# lst = list(map(float, input().split()))
# lst_abs = [abs(x) for x in lst]
# print(lst_abs)



# a = [x for x in range(-10, 10) if x % 2 == 0 and x < 0]
# print(a)

# '''линейная функция - увеличение на заданный шаг'''
# n = int(input())
# a = [3.5 * x + 2 for x in range(n)]
# print(a)


lst = [1 for x in range(11)]
print(lst)
#
# b = [1] * 7
# print(b)



