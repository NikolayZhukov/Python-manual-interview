numbers = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, numbers)
print(list(even))

numbers = [1, 2, 3, 4, 5, 6]
even = sorted(filter(lambda x: x % 2 == 0, numbers))
print(even)

numbers = [1, 2, 3, 4, 5, 6]
even = sorted([x for x in numbers if x % 2 == 0])
print(even)

numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
even.sort()
print(even)