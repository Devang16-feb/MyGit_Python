# 4. Write a program to find whether a given username contains less than 10 
# characters or not. 

username = input("Enter the Username")
if(len(username) < 10):
    print("username contains less than 10 characters!")
else:
    print("username contains greater than 10 characters!")