""""""
"""
Программа загадывает случайное число от 1 до 10. 
Пользователь должен угадать его. 
На каждой попытке программа подсказывает, больше или меньше названное число загаданного. 
Цикл продолжается, пока число не будет угадано. 
В конце выводится количество попыток.
"""
secret_number = 7
attempts = 0
while True:
    attempts += 1
    try:
        user_guess = int(input('Введите целое число: '))
        if user_guess < secret_number:
            print('Больше!')
        else:
            print('Меньше!')
    except ValueError:
        print('Ошибка')
        continue
    else:
        if user_guess == secret_number:
            break

print(f'Угадал! Секретное число = {secret_number}')
print(f'{attempts} попытки!')









