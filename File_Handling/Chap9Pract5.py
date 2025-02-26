# Repeat program 4 for a list of such words to be censored. 

words = ["Anushasan", "hathoda", "lota", "gadhe"]

with open("Censored.txt") as f:
    content = f.read()
   
for word in  words:
    content = content.replace(word, "#"*len(word))

with open("Censored.txt","w") as f:
    f.write(content)