"""
Тип ошибки 3: Отсутствие проверки типов в методе __add__ и прочих связанных с перегрузкой
стандартных операторов.
Если попытаться сложить объект класса с несоответствующим типом, Python выбросит ошибку.
"""
# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#
#     def __add__(self, other):
#         return Vector(self.x + other.x, self.y + other.y)  # Ошибка, если other не является объектом Vector.

"""
Решение:

Добавьте проверку типа для аргумента other в методе _add_.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError("Сложение возможно только между объектами класса Vector")
        return Vector(self.x + other.x, self.y + other.y)


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} лет"


print(Student("Иван", 22))
