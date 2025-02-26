# Write a python function to print multiplication table of a given number. 

def print_table(num):
    for i in range(1,11):
        print(num,"*",i,"=",num*i,"\n")

num = int(input("Enter number:"))
print_table(num)