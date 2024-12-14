# employee1 = ['Jin-Soo', 38, 'developer', 1200]
# employee2 = ['Lauren', 44, 'tester', 1000]

employee1 = {
    "name": "Lauren",
    "age": 44,
    "position": "developer",
    "salary": 1200
}

employee2 = {
    "name": "Jin-Soo",
    "age": 38,
    "position": "tester",
    "salary": 1000
}

def increase_salary(employee, percent):
    employee['salary'] += employee['salary'] * (percent/100)

def employee_info(employee):
    print(f"{employee['name']} is {employee['age']} years old. Employee is a {employee['position']} with the salary of ${employee['salary']}")

employees = [employee1, employee2]

increase_salary(employee2, 20)

for e in employees:
    employee_info(e)