marks={
    "Shivam" : "91",
    "Raghav": "87",
    "Suriya" : "69",
    0 : "Vishnu"
    }
print(marks,type(marks))
print(marks["Raghav"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Thakur":"40","Shivam": "100"})
print(marks)
print(marks.clear())
print(marks.popitem)