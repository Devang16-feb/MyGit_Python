# Create a class with a class attribute a; create an object from it and set ‘a’ 
# directly using ‘object.a = 0’. Does this change the class attribute? 


class MyClass:
    a = 10
    
o = MyClass()
print(o.a)
o.a = 0
print(o.a)

# No, this does not change the class attribute. It creates a new instance attribute;