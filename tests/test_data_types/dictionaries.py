"""
Добавить предметы в рюкзак в порядке убывания веса, пока не превысим лимит
"""
# N = int(input()) * 1000
#
# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# # Сортируем предметы по весу в порядке убывания
# sorted_items = sorted(things.items(), key=lambda x: x[1], reverse=True)
#
# result = []
# current_weight = 0
#
# # Добавляем предметы в рюкзак в порядке убывания веса, пока не превысим лимит
# for item, weight in sorted_items:
#     if current_weight + weight <= N:
#         result.append(item)
#         current_weight += weight
#
# # Выводим результат
# print(' '.join(result))


"""
Медик собирает аптечку, стараясь взять как можно больше разных видов медикаментов.
У каждого медикамента есть свой вес и приоритет важности (чем выше число, тем важнее).

Правила сборки:
1. Сначала брать самые важные медикаменты (по убыванию приоритета)
2. Если приоритет одинаковый - брать более легкие медикаменты сначала
3. Не превышать максимальный вес аптечки

Задача: 
Вывести список медикаментов, которые будут в аптечке, в порядке их добавления.

#Ожидаемый вывод
антибиотик обезболивающее йод жгут бинт антисептик шприц
"""
max_weight = 1500  # Максимальный вес аптечки в граммах

medicines = {
    'бинт': {'weight': 100, 'priority': 3},
    'антибиотик': {'weight': 200, 'priority': 5},
    'обезболивающее': {'weight': 150, 'priority': 5},
    'йод': {'weight': 50, 'priority': 4},
    'пластырь': {'weight': 80, 'priority': 2},
    'жгут': {'weight': 300, 'priority': 4},
    'антисептик': {'weight': 180, 'priority': 3},
    'вата': {'weight': 120, 'priority': 1},
    'шприц': {'weight': 60, 'priority': 3},
    'термометр': {'weight': 250, 'priority': 2}
}

max_weight = 1500

medicines = {
    'бинт': {'weight': 100, 'priority': 3},
    'антибиотик': {'weight': 200, 'priority': 5},
    'обезболивающее': {'weight': 150, 'priority': 5},
    'йод': {'weight': 50, 'priority': 4},
    'пластырь': {'weight': 80, 'priority': 2},
    'жгут': {'weight': 300, 'priority': 4},
    'антисептик': {'weight': 180, 'priority': 3},
    'вата': {'weight': 120, 'priority': 1},
    'шприц': {'weight': 60, 'priority': 3},
    'термометр': {'weight': 250, 'priority': 2}
}

# Сортируем медикаменты: сначала по приоритету (убывание), потом по весу (возрастание)
sorted_meds = sorted(medicines.items(),
                    key=lambda x: (-x[1]['priority'], x[1]['weight']))

result = []
current_weight = 0

for name, props in sorted_meds:
    if current_weight + props['weight'] <= max_weight:
        result.append(name)
        current_weight += props['weight']

print(' '.join(result))




# data = ([1,2,3],['a','b','c'])
# f, g = data
# dict = {f[i]: g[i] for i in range(len(data))}
# print(dict)


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
#
# sorted_items = things.items()
# print(sorted_items)


# things = {'карандаш': 20, 'зеркальце': 100, 'зонт': 500, 'рубашка': 300,
#           'брюки': 1000, 'бумага': 200, 'молоток': 600, 'пила': 400, 'удочка': 1200,
#           'расческа': 40, 'котелок': 820, 'палатка': 5240, 'брезент': 2130, 'спички': 10}
# sorted_items = sorted(things.items(), key=lambda x: x[1], reverse=True)
# print(sorted_items)


""""""
# Ввод максимального веса в кг и перевод в граммы






# import sys
# from collections import OrderedDict
#
# lst_in = list(map(str.strip, sys.stdin.readlines()))
#
# birthday_dict = OrderedDict()
#
# for line in lst_in:
#     if line:
#         day, name = line.split(maxsplit=1)
#         day = int(day)
#         if day in birthday_dict:
#             birthday_dict[day].append(name)
#         else:
#             birthday_dict[day] = [name]
#
# for day, names in birthday_dict.items():
#     print(f"{day}: {', '.join(names)}")


# numbers = list(map(int, input().split()))
# print(numbers)
# dict_numbers = dict.fromkeys(numbers)
#
# dict_numbers[555] = True
# print(dict_numbers)



# numbers = list(map(int, input().split()))
# unique_dict = {}
# unique_numbers = []
# for num in numbers:
#     if num not in unique_dict:
#         unique_dict[num] = True
#         unique_numbers.append(num)
# print(unique_dict)
# print(*unique_numbers)


# print(hash(("hello", "hello", "hello")))
# print(hash("hello"))


# cars = {'1': 'black', '2': 'white', '3': 'red'}
# for k in cars.items():
#     print(k)
#
# cars = {'1': 'black', '2': 'white', '3': 'red'}
# for k in cars.keys():
#     print(k)
#
# cars = {'1': 'black', '2': 'white', '3': 'red'}
# for k in cars.values():
#     print(k)
from venv import create

# cars = {'1': 'black', '2': 'white', '3': 'red'}
# print(cars['2'])

# cars = {'1': 'black', '2': 'white', '3': 'red'}
# cars['2'] = 'blue'
# print(cars)
#
# cars = {'1': 'black', '2': 'white', '3': 'red'}
# del(cars['2'])
# print(cars)

