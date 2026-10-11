def combine_employee_data(names, positions, salaries):
    combined = zip(names, positions, salaries)
    return list(map(lambda data: f'Имя: {data[0]} - должность {data[1]} - зарпалата: {data[2]}', combined))


if __name__ == '__main__':
    emp_data = [
        ["Анна", "Борис", "Виктория"],
        ["Менеджер", "Разработчик", "Аналитик"],
        [80000, 120000, 90000]
    ]
    for employee in combine_employee_data(*emp_data):
        print(employee)
