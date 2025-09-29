numbers = tuple(map(int, input().split()))
numbers = list(numbers)
index_list_not_unique = []

for i, num in enumerate(numbers):
    if numbers.count(num) > 1:
        index_list_not_unique.append(i)

print(*index_list_not_unique)




# numbers = tuple(map(int, input().split()))
# numbers_unique = []
# for num in numbers:
#     if num not in numbers_unique:
#         numbers_unique.append(num)
# numbers = tuple(numbers_unique)
# print(*numbers_unique)


# lst1 = input().split()
# lst2 = [[lst1[i], int(lst1[i+1])] for i in range(0, len(lst1), 2)]
# print(lst2)



# lst1 = list(map(int, input().split()))
# lst2 = list(map(int, input().split()))
# list_sum = [lst1[i] + lst2[i] for i in range(len(lst1))]
# print(*list_sum)


# numbers = list(map(float, input().split()))
# result = [numbers[i] for i in range(len(numbers)) if i % 2 == 0]
# print(*result)

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


# cities = ["Mosca", "Londra", "Napoli", "Sanpietroburgo", "Amsterdam", "Manchester"]
#
# cities_selected = [x for x in cities if len(x) < 9]
# print(cities_selected)

# a = [x for x in range(-10, 10) if x % 2 == 0 and x < 0]
# print(a)

# '''линейная функция - увеличение на заданный шаг'''
# n = int(input())
# a = [3.5 * x + 2 for x in range(n)]
# print(a)


# lst = [1 for x in range(11)]
# print(lst)
#
# b = [1] * 7
# print(b)


# n = int(input())
# sum = [x ** 2 for x in range(n)]
# print(sum)
