# Write a python function which converts inches to cms.

def inches_to_cms(inches):
    return inches * 2.54

inch = float(input("Enter length in inches:"))
centimeter = inches_to_cms(inch)
print(f"{inch} inches is equal to {centimeter} cms")