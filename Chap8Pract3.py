# Write a recursive function to calculate the sum of first n natural numbers. 

def sum(n):
    if n == 0:
        return 0
    else:
        return n + sum(n-1)

print("sum of n naturaul number is :",sum(5))