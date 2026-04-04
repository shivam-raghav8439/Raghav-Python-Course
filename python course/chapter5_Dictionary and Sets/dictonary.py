marks = {
    "Shivam" : "100",
    "Raghav" : "98",
    "Suriya" : "95",
}
print(marks, type(marks))
print(marks["Raghav"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Shivam":"99", "Rajput":"70"})
print(marks)
print(marks.get("Rajput"))
print(marks["Rajput"])
print(marks.get("Rajput2"))
print(marks["Rajput2"])