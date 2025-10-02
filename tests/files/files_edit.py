''' '''

# try:
#     with open('out.txt','a+') as file:
#         file.seek(0)
#         s = file.readline()
#         print(s)
# except:
#     print('Ошибка при работе с файлом')


"""Записывает данные в бинарном режиме доступа"""

# import pickle
#
# book1 = ["Евгений Онегин", "Пушкин А.С.", 200]
# book2 = ["Муму", "Тургенев И.С.", 250]
# book3 = ["Мастер и Маргарита", "Булгаков М.А.", 500]
# book4 = ["Мертвые души", "Гоголь Н.В.", 190]
#
# try:
#     with open("out.bin", "wb") as file:
#         pickle.dump(book1, file)
#         pickle.dump(book2, file)
#         pickle.dump(book3, file)
#         pickle.dump(book4, file)
# except:
#     print("Ошибка при работе с файлом")


"""Считывает данные в бинарном режиме доступа"""
# import pickle
#
# try:
#     with open("out.bin", "rb") as file:
#         b1 = pickle.load(file)
#         b2 = pickle.load(file)
#         b3 = pickle.load(file)
#         b4 = pickle.load(file)
# except:
#     print("Ошибка при работе с файлом")
#
# print(b1, b2, b3, b4, sep="\n")