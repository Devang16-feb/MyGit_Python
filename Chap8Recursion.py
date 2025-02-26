#Find Factorial

def factorial(num):
    if(num == 0):
        return 1
    else:
        return num * factorial(num-1)

fact = factorial(5)
print(f"Factorial of number is: {fact}")    