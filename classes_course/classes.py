class Employee:
    def __init__(self, name, age, position, salary):
        self.name = name
        self.age = age
        self.position = position
        self.salary = salary
        self._annual_salary = None

    def __str__(self):
        return f"{self.name} is {self.age} years old. Employee is a {self.position} with the salary of ${self.salary}"

    def __repr__(self):
        return (
             f"Employee("
             f"{repr(self.name)}, {repr(self.age)},"
             f"{repr(self.position)}, {repr(self.salary)})"
        )
    
    def increase_salary(self, percent):
        self.salary += self.salary * (percent/100)

    @property
    def salary(self):
        return f"${self._salary}"
    
    @salary.setter
    def salary(self, salary):
        if salary < 1000:
            raise ValueError('Minimum wage is $1000')
        self._annual_salary = None
        self._salary = salary

    @property
    def annual_salary(self):
        if self._annual_salary is None:
            self._annual_salary = self.salary * 12
        return self._annual_salary

employee1 = Employee("Ji-Soo", 38, 'developer', 1200)
employee2 = Employee("Lauren", 44, 'tester', 1000)

# employee2.increase_salary(20)
# print(employee1)
# print(eval(repr(employee1)))
# employee1.salary = 2000
# print(employee1.salary)

