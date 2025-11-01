""""""
"""filter"""
# numbers = [1, 5, 3, 4, 2, 6]
# even = filter(lambda x: x % 2 == 0, numbers)
# print(list(even))
#
"""'это эквивалентно"""
# numbers = [1, 5, 3, 4, 2, 6]
# even = []
# for x in numbers:
#     if x % 2 == 0:
#         even.append(x)

# """list comprehension"""
# numbers = [1, 5, 3, 4, 2, 6]
# even = [x for x in numbers if x % 2 == 0]
# print(list(even))

# """sorted + filter"""
# numbers = [1, 5, 3, 4, 2, 6]
# even = sorted(filter(lambda x: x % 2 == 0, numbers))
# print(even)

# """sorted"""
# numbers = [1, 2, 3, 4, 5, 6]
# even = sorted([x for x in numbers if x % 2 == 0])
# print(even)

# """sort"""
# numbers = [1, 5, 3, 4, 2, 6]
# even = [x for x in numbers if x % 2 == 0]
# even.sort()
# print(even)



"""
Дан список слов: words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
Оставь только те слова, которые начинаются с буквы “a” и имеют длину больше 3 символов.
"""
"""filter"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = filter(lambda x: x[0] == 'a' and len(x) > 3, words)
# print(list(words_filtered))

"""for"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = []
# for x in words:
#     if x[0] == 'a' and len(x) > 3:
#         words_filtered.append(x)
# print(words_filtered)


"""list comprehension"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = [x for x in words if x[0] == 'a' and len(x) > 3]
# print(words_filtered)

"""sort"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = [x for x in words if x[0] == 'a' and len(x) > 3]
# words_filtered.sort()
# print(words_filtered)

"""
sorted - САМЫЙ ПИТОНОВСКИЙ СПОСОБ, т.к.: 
1) list comprehension, а не lambda (немного устаревший, менее читаемый) 
2) sorted, а не sort, т.к. создаёт новый список, а не меняет исходный, работает не только со списками
"""

# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = sorted([x for x in words if x[0] == 'a' and len(x) > 3])
# print(words_filtered)

# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = sorted([x for x in words if x[0] == 'a' and len(x) > 3])
# print(words_filtered)


"""
Дан список слов: words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
Оставь только те слова, которые начинаются с буквы “a”, имеют длину больше 3 символов и отсортируй их по длине по возрастанию.
"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = sorted([x for x in words if x[0] == 'a' and len(x) > 3], key=len)
# print(words_filtered)

"""
Дан список слов: words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
Оставь только те слова, которые начинаются с буквы “a”, имеют длину больше 3 символов 
и отсортируй по последней букве в алфавитном порядке по убыванию.
"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
# words_filtered = sorted(
#     [x for x in words if x[0] == 'a' and len(x) > 3],
#     key=lambda x: x[-1],
#     reverse=True
# )
# print(words_filtered)

"""
Обычная функция вместо lambda
"""
# words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]
#
# def last_letter(word):
#     return word[-1]
#
# words_filtered = sorted(
#     [x for x in words if x[0] == 'a' and len(x) > 3],
#     key=last_letter,
#     reverse=True
# )
# print(words_filtered)

"""
Обычная функция + последняя буква отдельно
"""
words = ["apple", "ant", "banana", "avocado", "axe", "air", "alpha"]

def last_letter(word):
    return word[-1]

data = [x for x in words if x[0] == 'a' and len(x) > 3]
decorated = [(last_letter(x), x) for x in data]
print(decorated)
# print(data)
