# Write a program to read the text from a given file ‘poems.txt’ and find out 
# whether it contains the word Thor

f = open("poems.txt")
c = f.read()

if("Thor" in c):
    print("The file contains the word Thor")
else:
    print("The file does not contain the word Thor")
f.close()