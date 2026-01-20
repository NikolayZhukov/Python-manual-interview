""""""
"""
Наследование + абстракция + полиморфизм
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

dog = Dog("Бобик")
cat = Cat("Маруся")

print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!


"""
Автомобили б/у
"""
class Car:
    def __init__(self, model, year, fuel, comment, color):
        self.model = model #Передаётся при вызове, при инициализации экземпляра класса
        self.year = year
        self.fuel = fuel
        self.comment = comment
        self.color = color

    def calculate_price(self):
        raise NotImplementedError('Отсутствует метод drive')

    def comment_from_vendor(self):
        raise NotImplementedError

class ElectricCar(Car):
    def __init__(self, model, year, comment, color):
        super().__init__(model, year, 'Электричество', comment, color)

    def calculate_price(self):
        price = 50000 - ((2025 - self.year) * 1000)
        return f'Actual price of {self.model}, {self.year} года = {price} $'

    def comment_from_vendor(self):
        return f'\nКомментарий от продавца: {self.comment}'

class PetrolCar(Car):
    def __init__(self, model, year, comment, color):
        super().__init__(model, year,'Бензин', comment, color)

    def calculate_price(self):
        price = 30000 - ((2025 - self.year) * 1000)
        return f'Actual price of {self.model}, {self.year} года = {price} $'

    def comment_from_vendor(self):
        return f'\nКомментарий от продавца: {self.comment}'

eleсtric_car = ElectricCar('Tesla M50', 2022, 'В отличном состоянии, как новая', color='синий')
petrol_car = PetrolCar('Lada 777', 2005, 'Не заводится, в последний раз ездил на ней 3 года назад', color='чёрный')

print(eleсtric_car.calculate_price(), eleсtric_car.comment_from_vendor())
print(eleсtric_car.color)
print(petrol_car.calculate_price(), petrol_car.comment_from_vendor(), petrol_car.color)
print(petrol_car.color)

# print(eleсtric_car.__dict__)
# print(petrol_car.__dict__)









# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Cat:
#     def speak(self):
#         return "Meow"
#
# class Dog:
#     def speak(self):
#         return "Woof"
#
# def make_animal_speak(animal):
#     print(animal.speak())
#
# cat = Cat()
# dog = Dog()
#
# make_animal_speak(cat)  # Вывод: Meow
# make_animal_speak(dog)  # Вывод: Woof
# print(dog.speak())  # Buddy says Woof!
# print(cat.speak())  # Whiskers says Meow!




# class ParentClass:
#     def __init__(self, name):
#         self.name = name
#
#     def greet(self):
#         print(f"Hello, my name is {self.name}")
#
# # child = ParentClass('Matteo')
# # child.greet()
#
# class ChildClass(ParentClass):
#     def __init__(self, name, age):
#         super().__init__(name)
#         self.age = age
#
#     def greet(self):
#         super().greet()
#         print(f"I am {self.age} years old")
#
# child = ChildClass("Simone", 88)
# child.greet()