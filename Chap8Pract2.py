# Write a python program using function to convert Celsius to Fahrenheit. 

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

cel = float(input("Enter temperature in Celsius:"))

far = celsius_to_fahrenheit(cel)
print(f"{cel} Celsius is equal to {far} Fahrenheit")