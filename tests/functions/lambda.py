""""""
"""
Отсортировать список строк по последнему символу
# words = ['apple', 'banana', 'cherry', 'date']
"""
words = ['apple', 'banana', 'cherry', 'date']
sorted_words = sorted(words, key=lambda x: x[-1], reverse=True)
print(sorted_words)





















# words = ['apple', 'banana', 'cherry', 'date']
# sorted_words = sorted(words, key=lambda x: x[-1])
# print(sorted_words)



"""
Отсортировать список строк по первому символу
"""
# words = ['apple', 'banana', 'cherry', 'date']
# sorted_words = sorted(words, key=lambda x: x[0])
# print(sorted_words)



"""
Отсортировать список словарей по значению ключа
"""
# students = [
#     {'name': 'Alice', 'grade': 85},
#     {'name': 'Bob', 'grade': 92},
#     {'name': 'Charlie', 'grade': 78}
# ]
# sorted_students = sorted(students, key=lambda x: x['grade'])
# print(sorted_students)



"""
Сортировка по длине строки, а при равной длине - по алфавиту
"""
# words = ['cat', 'apple', 'dog', 'banana', 'elephant']
# sorted_words = sorted(words, key=lambda x: (len(x), x))
# print(sorted_words)