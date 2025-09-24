# def process_data(data):
#     result = data.upper()
#     return result
# print(process_data("hello"))

def process_data(data):
    result = None
    if data is not None:
        result = data.upper()
    return result
print(process_data("hello"))

def process_data(data):
    if data is None:
        return None
    return data.upper()
print(process_data("Ciao!"))

def process_data(data):
    return data.upper() if data is not None else None
print(process_data("Welcome!"))


# def process_data(data_1, data_2):
#     result_1 = None
#     result_2 = None  # Инициализация переменной
#
#
#     if data_1 is not None and data_2 is not None:
#         result_1 = data_1.upper()  # Обработка данных
#         result_2 = data_2.lower()  # Обработка данных
#
#         print(hex(id(result_1)))
#
#     return result_1, result_2
#
#
# # Использование
# # print(process_data("hello"))  # HELLO
# # print(process_data(None))  # None
# print(process_data("TesTdaTa", "asdEWWERFaasdaDFSD"))
