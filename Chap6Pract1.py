#. Write a program to find the greatest of four numbers entered by the user. 

num1 = int(input("Enter 1st nnumber:"))
num2 = int(input("Enter 1st nnumber:"))
num3 = int(input("Enter 1st nnumber:"))
num4 = int(input("Enter 1st nnumber:"))

if(num1 > num2 and num1 > num3 and num1 > num4):
    print(f"Greter number among four elements is {num1}")
elif(num2 > num1 and num2 > num3 and num2 > num4):
    print(f"Greter number among four elements is {num2}")
elif(num3 > num1 and num3 > num2 and num3 > num4):
    print(f"Greter number among four elements is {num3}")
else:
     print(f"Greter number among four elements is {num4}")
        