class Empolyee:
    no_of_leaves=8

    def printdetails(self):
        return f"Name is {self.name}.salary is {self.salary} and role is {self.role}"

harry=Empolyee()
rohan=Empolyee()

harry.name="Harry"
harry.salary=455
harry.role="Instructor"

rohan.name="Rohan"
rohan.salary=555
rohan.role="student"

print(rohan.printdetails())
print(harry.printdetails())