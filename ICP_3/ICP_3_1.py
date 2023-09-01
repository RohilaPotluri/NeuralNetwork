# Employee class
class Employee:
    count = 0  # for the count of employees
    employees = []  # for the list of employees

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.count = Employee.count + 1  # count gets incremented each time when employee instance is called
        Employee.employees.append(self)  # Appending employee details to list

    def average_salary(self):         # function to calculate average_salary of the employees
       return sum(employee.salary for employee in Employee.employees) / Employee.count


class Fulltime_Employee(Employee): # Full time Employee class inheriting the Employee class
   pass

# creating instances for above classes
employee1 = Employee("Jay", "Pang", 95000, "Finance")
employee2 = Employee("Kay", "Smith", 87000, "CS")
fulltime_employee1 = Fulltime_Employee("Idan", "Fareen", 98000, "Management")

# Accessing the classes using instances
print(employee1.average_salary())
print(employee2.average_salary())
print(fulltime_employee1.average_salary())
print(Employee.count)

