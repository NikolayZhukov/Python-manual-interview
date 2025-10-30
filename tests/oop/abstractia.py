from abc import ABC, abstractmethod

class Book(ABC):
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @abstractmethod
    def get_summary(self):
        pass

    # def get_summary(self):
    #     raise NotImplementedError("Subclass must implement abstract method")

class Fiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - роман в стиле исторический фикшн, автор - {self.author}')

class NonFiction(Book):
    def get_summary(self):
        print(f'"{self.title}" - книга в стиле нон фикшн, автор - {self.author}')

# class Poetry(Book):
#     pass


book1 = Fiction('Будни', 'Петров')
print(book1.get_summary())