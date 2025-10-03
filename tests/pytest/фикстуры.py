import pytest
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person: {self.name}, {self.age}"  # Added "years old"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"


person = Person("Alice", 25)

print(str(person))   # Output: Person: Alice, 25 years old
print(repr(person))  # Output: Person('Alice', 25)



# import pytest
#
# # фикстура
# @pytest.fixture
# def sample_data():
#     print("\nВыполняется фикстура перед тестом")  # выполняется перед тестом
#     data = [1, 2, 3]
#     return data
#
# # тест с использованием фикстуры
# def test_sum(sample_data):
#     assert sum(sample_data) == 6




