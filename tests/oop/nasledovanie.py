class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Cat:
    def speak(self):
        return "Meow"

class Dog:
    def speak(self):
        return "Woof"

def make_animal_speak(animal):
    print(animal.speak())

cat = Cat()
dog = Dog()

make_animal_speak(cat)  # Вывод: Meow
make_animal_speak(dog)  # Вывод: Woof
print(dog.speak())  # Buddy says Woof!
print(cat.speak())  # Whiskers says Meow!



# class Animal:
#     def __init__(self, name):
#         self.name = name
#
#     def speak(self):
#         raise NotImplementedError("Subclass must implement abstract method")
#
# class Dog(Animal):
#     def speak(self):
#         return f"{self.name} says Woof!"
#
# class Cat(Animal):
#     def speak(self):
#         return f"{self.name} says Meow!"
#
# dog = Dog("Бобик")
# cat = Cat("Маруся")
#
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