marks = {
    "Devang" : 100,
    "Shubham" : 56,
    "Rohan" : 23
}

print(marks, type(marks))
print(marks["Devang"])

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Devang" : 99})
print(marks)
print(marks.get("Devang"))