
class Employee: # Base class
    company = "Google"
    
    def showDetails(self):
        print(f"the name is {self.name} and the salary is {self.salary}")

class Programmer(Employee):
    company = "Microsoft"
    
    def showLaguage(self):
        print(f"The name is {self.name} and the salary is {self.salary}. He knows {self.language}.")
        
        
a = Employee()
b = Programmer()