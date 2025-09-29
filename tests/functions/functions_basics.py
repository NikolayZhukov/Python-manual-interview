def print_frase():
    name, surname, *rest = input().split()
    print(f"Уважаемый, {name} {surname}! Вы верно выполнили это задание!")

print_frase()

