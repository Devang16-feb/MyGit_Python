# Write a program to find out the line number where python is present from ques 6.



with open("log.txt") as f:
    lines = f.readlines()
    
lineo = 1    
for line in lines :
    if("python" in line):
        print(f"Python is present in line {lineo}")
        break # if Break then it will print only first line where python is present
    lineo += 1
else:
    print("Python is not present in the log file")