f = open("file.txt") 
lines = f.readlines()

while(lines != ""):
    print(lines)
    lines = f.readlines()
    
f.close()

