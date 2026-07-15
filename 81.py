# save student info to a file 

class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("Marks: ", self.marks)
        

name = input("enter the name: ")
age = int(input("enter the age: "))
marks = float(input("enter the marks: "))

student1 = Student(name, age, marks)
student1.display()

with open("student.txt", "w") as f:
    f.write(f"Name: {student1.name}\n")
    f.write(f"Age: {student1.age}\n")
    f.write(f"Marks: {student1.marks}\n")
    f.write("\n")

with open("student.txt", "r") as f:
    print("-"*20)
    print("student details")
    print("-"*20)
    print(f.read())

print("program ended here")    








#ef to_dict(self):
#        return {
#           "Name": self.name,
#          "Age": self.age,
#         "Marks": self.marks
#    }

# # Save as JSON
# with open("student.json", "w") as f:
#     json.dump(student1.to_dict(), f, indent=4)

# # Read back the JSON
# with open("student.json", "r") as f:
#   print("student details (JSON)")
#  print(f.read())

#print("program ended here")