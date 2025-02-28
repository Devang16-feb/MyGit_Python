# Can you change the self-parameter inside a class to something else (say 
# “harry”). Try changing self to “slf” or “harry” and see the effects. 

class Employee:
    def __init__(harry, name, salary, subunit):
        harry.name = name
        harry.salary = salary
        harry.subunit = subunit
        print("Employee is created!")
        
    def getDetails(harry):
        print(f"The name of the employee is {harry.name}")

self = Employee("Harry", 1000000, "YouTube")
self.getDetails() # Employee.getDetails(harry)


# here inseted of self i have used harry and it is working fine.