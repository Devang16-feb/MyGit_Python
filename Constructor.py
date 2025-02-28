class Employee:
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Employee is created!")
        
    def getDetails(self):
        print(f"The name of the employee is {self.name}")
        print(f"The salary of the employee is {self.salary}")
        print(f"The subunit of the employee is {self.subunit}")
        
    @staticmethod
    def greet():
        print("Good Morning, Sir")
        
harry = Employee("Harry", 1000000, "YouTube")
harry.getDetails() # Employee.getDetails(harry)
harry.greet() # Employee.greet() static method