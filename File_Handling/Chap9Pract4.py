# A file contains a word Marvel multiple times. You need to write a program 
# which replace this word with ##### by updating the same file. 

word = "Marvel"

with open("marvel_ous.txt") as f:
    content = f.read()
    
contentNew = content.replace(word, "#####")

with open("marvel_ous.txt","w") as f:
    f.write(contentNew)