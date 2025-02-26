# Write a program to find out whether a file is identical & matches the content of 
# another file.

f = open("this.txt")
content1 = f.read()

f = open("this_copy.txt")
content2 = f.read()

if(content1 == content2):
    print("Files are identical")
else:
    print("Files are not identical")