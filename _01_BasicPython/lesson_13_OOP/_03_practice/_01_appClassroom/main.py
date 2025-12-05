"""
Задача 1: Управление классами в школе

Ситуация: представьте, что вы — классный руководитель и хотите автоматизировать процесс учёта учеников.
Нам нужно создать программу, которая позволит добавлять учеников в класс,
ставить им оценки и видеть список всех учеников с их средними баллами.

Задача: создайте программу, которая позволяет:

Добавлять учеников в список класса.
Присваивать оценки ученикам.
Просматривать всех учеников с их средними баллами.
Шаги реализации:

"""

from classes.ClassStudent import Student
from classes.ClassClassroom import Classroom

if __name__ == '__main__':
    classroom = Classroom()
    while True:
        command = input("Введите команду (1 - add_student, 2 - add_grade, 3 - show_students, 0 - exit): ").strip().lower()
        if command == '1':
            name = input('Введите имя студента: ').strip().title()
            student = Student(name)
            classroom.add_student(student)
            # classroom.add_student(Student(name))
            print(f'Студент {name} добавлен')
        elif command == '2':
            name = input(f'Введите имя студента: ').strip().title()
            grade = float(input('Введите оценку: '))
            print(classroom.add_grade_to_student(name, grade))
        elif command == '3':
            classroom.show_students()
        elif command == '0':
            print(f'Программа завершена.')
            break
        else:
            print('Неизвестная команда. Попробуйте снова.')
