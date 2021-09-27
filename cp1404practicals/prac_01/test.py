class Student:
    def __init__(self, first_name="", last_name="", student_id=0):
        self.first_name = first_name
        self.last_name = last_name
        self.id = student_id

    def __str__(self):
        return "{} {} ({})".format(self.first_name, self.last_name, self.id)


first_name = input("First name: ")
last_name = input("Last name: ")
student_id = int(input("ID: "))
s1 = Student(first_name, last_name, student_id)
print(s1.first_name, "has ID", s1.id)
