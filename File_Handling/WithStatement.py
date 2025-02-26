# Open the file in read mode using 'with', which automatically closes the file 
with open("Myfile.txt", "r") as f: 
    # Read the contents of the file 
    text = f.read() 
    # Print the contents 
print(text) 

#Dont hava to close the file, it is automatically closed