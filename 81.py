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


while True:
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    marks = float(input("Enter the marks: "))

    student1 = Student(name, age, marks)

    print("\nStudent Details")
    print("-" * 20)
    student1.display()

    # Append student details to file
    with open("student.txt", "a") as f:
        f.write(f"Name: {student1.name}\n")
        f.write(f"Age: {student1.age}\n")
        f.write(f"Marks: {student1.marks}\n")
        f.write("-" * 20 + "\n")

    choice = input("\nDo you want to add another student? (yes/no): ").lower()

    if choice != "yes":
        break


# Read all student details from file
with open("student.txt", "r") as f:
    print("\n" + "-" * 20)
    print("Student Details")
    print("-" * 20)
    print(f.read())

print("Program ended here")









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