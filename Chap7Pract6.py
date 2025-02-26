# Write a program to calculate the factorial of a given number using for loop. 

num = int(input("Enter number:"))

fact = 1
while(num>0):
    fact *= num
    num -= 1
print("Factorial of number is:",fact)