#  Write a program using functions to find greatest of three numbers. 

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>c and b>a):
        return b
    else:
        return c

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
c = int(input("Enter third number:"))

result = greatest(a,b,c)
print(f"Greatest of {a},{b} and {c} is {result}")