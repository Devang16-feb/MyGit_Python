# Create a class “Programmer” for storing information of few programmers 
# working at Microsoft. 

class Programmer:
    company = "Microsoft"
    def __init__(self, name, salary, subunit):
        self.name = name
        self.salary = salary
        self.subunit = subunit
        print("Programmer is created!")

harry = Programmer("Harry", 1000000, "Azure")
print(harry.name, harry.salary, harry.subunit)