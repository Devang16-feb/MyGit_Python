#  Write a program to find out whether a student has passed or failed if it requires a 
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
# take marks as an input from the user. 

Math = int(input("Enter Math marks"))
Marathi = int(input("Enter Marathi marks"))
Hindi = int(input("Enter Hindi marks"))

total_percentage = ((Math + Marathi + Hindi)/300)*100

if(total_percentage >= 40):
    print("You are Paas... Total percentage is:",total_percentage)
else:
    print("You are Fail..Total percentage is",total_percentage)
    
# for each subject:

if((Math/100)*100 >= 33):
    print("Pass in Math")
else:
    print("Fail in Math")

if((Marathi/100)*100 >= 33):
    print("Pass in Marathi")
else:
    print("Fail in Marathi")

if((Hindi/100)*100 >= 33):
    print("Pass in Hindi")
else:
    print("Fail in Hindi")