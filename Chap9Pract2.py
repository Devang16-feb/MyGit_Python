# Write a class “Calculator” capable of finding square, cube and square root of a 
# number. 

class Calculator:
    def __init__(self, number):
        self.number = number
        print("Number is created!")
    
    def square(self):
        print(f"The square of {self.number} is {self.number**2}")
    def cube(self):
        print(f"The cube of {self.number} is {self.number**3}")
    def squareRoot(self):
        print(f"The square root of {self.number} is {self.number**0.5}")
        
num = Calculator(9)
num.square()
num.cube()
num.squareRoot()