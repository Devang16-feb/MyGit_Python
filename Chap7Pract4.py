# Write a program to find whether a given number is prime or not. 

num = int(input("Enter number:"))

if(num<=1):
    print("Number is not prime")
else:
    i=2
    while(i<num):
        if(num%i == 0):
            print("Number is not prime")
            break
        i+=1
    if(i==num):
        print("Number is prime")