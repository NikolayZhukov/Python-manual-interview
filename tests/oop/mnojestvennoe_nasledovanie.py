class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "Неизвестный звук"

    def eat(self):
        return f"{self.name} ест"


class Mammal:
    def __init__(self, has_fur=True):
        self.has_fur = has_fur

    def feed_milk(self):
        return "Кормит детенышей молоком"

    def breathe(self):
        return "Дышит легкими"


class Bird:
    def __init__(self, can_fly=True):
        self.can_fly = can_fly

    def fly(self):
        if self.can_fly:
            return "Летает"
        return "Не может летать"

    def lay_eggs(self):
        return "Откладывает яйца"


# Класс с множественным наследованием
class Bat(Animal, Mammal, Bird):
    def __init__(self, name):
        Animal.__init__(self, name)
        Mammal.__init__(self)
        Bird.__init__(self, can_fly=True)

    # def speak(self):
    #     return "Пищит"

    def use_echolocation(self):
        return "Использует эхолокацию"


# Использование
bat = Bat("Бэтмен")
print(bat.speak())  # Пищит
print(bat.eat())  # Бэтмен ест
print(bat.feed_milk())  # Кормит детенышей молоком
print(bat.fly())  # Летает
print(bat.use_echolocation())  # Использует эхолокацию