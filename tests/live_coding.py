""""""
"""
 Программа запрашивает у пользователя слова до тех пор, пока он не введет слово "стоп", регистронезависимо. 
 После этого выводится количество введенных слов и сами слова.
"""
words = []
while True:
    user_input = input()
    if user_input.lower() == "стоп":
        break
    else:
        words.append(user_input)

print(len(words), *words)










