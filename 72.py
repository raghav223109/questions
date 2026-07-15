student = {
    "name":"raghav",
    "age":22,
    "course":"pyhton"
}
print(student)
print(student["name"])
print(student["age"])
print(student["course"])
print(len(student))
student["age"] = 21
student["city"] = "delhi"
print(student)
student.pop("age")
print(student)