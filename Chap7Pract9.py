#  Write a program to print multiplication table of n using for loops in reversed 
# order. 

n = int(input("Enter number:"))

i = 10
for i in range(10, 0, -1):
    print(n, "*", i, "=", n*i, "\n")
    i -= 1