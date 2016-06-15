import Employee

countent = help(Employee)

print countent
countent1 = dir(Employee.__package__)
print countent1

emp1 = Employee("Zara", 2000)
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
