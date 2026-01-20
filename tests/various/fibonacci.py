""" """
"""
Напишите программу, которая для заданного натурального числа n выводит n-ное число последовательности Фибоначчи.
Определение:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2) для всех n > 1.
"""

# n = 10
# fibonacci_list = [0, 1]
# list_fib = [fibonacci_list[-1] + fibonacci_list[-2] for x in range(2, n+1)]
# fibonacci_list.extend(*list_fib)
#
# print(fibonacci_list)

n = 10

fibonacci_numbers = [0, 1]

for i in range(2, n + 1):
    # Каждый раз берём актуальные последние значения
    next_num = fibonacci_numbers[-1] + fibonacci_numbers[-2]
    fibonacci_numbers.append(next_num)

print(f"Полная последовательность: {fibonacci_numbers}")
print(f"F({n}) = {fibonacci_numbers[-1]}")
