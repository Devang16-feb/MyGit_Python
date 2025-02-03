# 5. Write a program which finds out whether a given name is present in a list or not. 

name = input("Enter the name:")
list = ["Apple", "Orange", 5, 345.06, False, "Aakash", "Rohan"]

if(list.__contains__(name)):
    print("Name is present in list")
else:
    print("Name is not present in list")
    