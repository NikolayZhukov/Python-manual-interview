from pathlib import Path

p = Path('out.txt')
absolute_path = p.resolve()                     #/home/nikolay/PycharmProjects/MDM/tests - путь до текущей директории
parent_dir = p.resolve().parent                 #/home/nikolay/PycharmProjects/MDM - путь до родительской директории
parent_parent_dir = p.resolve().parent.parent   #/home/nikolay/PycharmProjects

# print(absolute_path)
print(p.read_text())


"""
1) resolve() - это встроенный метод класса Path в модуле pathlib, делает путь абсолютным
2) path() без resolve() - возвращает относительный путь
"""