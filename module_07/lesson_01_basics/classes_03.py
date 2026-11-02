class Student:
    def __init__(self, name, surname, course):
        self.name = name
        self.surname = surname
        self.course = course
        self.marks = {}

    def add_mark(self, discipline, mark):
        self.marks[discipline] = mark
        print(f'{self.name} {self.surname}, получил по курсу: {self.course}, предмет: {discipline}, оценку {mark}')

    def display_student_marks(self):
        print(f'Студент: {self.name} {self.surname}.\nКурс: {self.course}')
        for discipline, mark in self.marks.items():
            print(f'Предмет: {discipline} >> {mark}')


if __name__ == '__main__':
    students = [
        ['Иван', 'Иванов', 'Python'],
        ['Петр', 'Петров', 'QA'],
    ]
    students_objects = []
    for s_name, s_surname, s_course in students:
        students_objects.append(Student(s_name, s_surname, s_course))

    student1, student2 = students_objects
    student1.add_mark('Строки', 8)
    student1.add_mark('Списки', 9)
    student1.add_mark('Словари', 7)
    student1.display_student_marks()
    print(student1.marks)
    print()

    student2.add_mark(10, 'Ручное тестирование')
    student2.add_mark(9, 'Основы python')
    student2.add_mark(7, 'Базы данных')
    student2.display_student_marks()

