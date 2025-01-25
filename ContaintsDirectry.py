# WAPP to print containts of directory using os module
# Serach online for search that function  which does that

import os

# Get the directory path from the user
directory_path = '/'

# List all contents in the directory
contents = os.listdir(directory_path)
print("\nContents of the directory:")

# print each file and directory name
for item in contents:
    print(item)