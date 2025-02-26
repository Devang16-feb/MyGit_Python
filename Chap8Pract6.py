# Write a python function to remove a given word from a list ad strip it at the same 
# time. 

def remove_word(lst,word):
    for i in range(len(lst)):
        if(lst[i] == word):
            lst.pop(i)
            break
    return lst
list1 = ["apple","banana","cherry","apple","date"]
remove_word(list1,"apple")
print(list1)