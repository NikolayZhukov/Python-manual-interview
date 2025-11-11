""""""
def decorator_with_arguments(show_before, show_after):
    def greet_str_decorator(func):
        def wrapper(*args, **kwargs):
            text = func(*args, **kwargs)
            if show_before:
                print('До декорируемой функции')
            result = f'Привет, {text}'
            print(f'Result = {result}')
            if show_after:
                print('После декорируемой функции')
            return result
        return wrapper
    return greet_str_decorator

@decorator_with_arguments(show_before=False, show_after=False)
def get_string(name, surname):
    return f'{name} {surname}'

name = input('Введите имя: ')
get_string(name, surname='Петров')













