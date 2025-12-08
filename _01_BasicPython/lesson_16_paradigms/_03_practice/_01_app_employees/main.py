from classes.ClassEmployee import Employee, Manager, TopManager, Intern

if __name__ == '__main__':
    try:
        employees = [
            Employee("Иван", "Иванов", 50000),
            Manager("Мария", "Петрова", 80000, 20000),
            TopManager("Александ", "Дмитриев", 80000, 20000, 1.3),
            Intern("Алексей", "Смирнов", 30000, 0.5)
        ]
    except ValueError as ve:
        print(ve)
    else:
        for emp in employees:
            print(f'{emp.get_info()} - Зарплата: {emp.salary:.2f}')
