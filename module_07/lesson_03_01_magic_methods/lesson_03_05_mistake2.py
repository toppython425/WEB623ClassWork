"""
Тип ошибки 2: Отсутствие возврата строки в __str__
Возникает, когда метод __str__ возвращает не строку, а объект другого типа, например, int.
"""
# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def __str__(self):
#         return self.age  # Ошибка: возвращается число, а не строка.


# print(Student("Иван", 22))

"""
Решение:

Метод _str_ всегда должен возвращать строку.
"""


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"


print(Student("Иван", 22))
