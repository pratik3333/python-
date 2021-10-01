

           #Single level inheritance
class Employee:
    number_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role
        self.email=name+'123@gmail.com'

    def printdetails(self):
        return f"The name is {self.name}.\nThe salary is {self.salary}.\n The Role is {self.role}."

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.number_of_leaves=new_leaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

class Programmer(Employee):
    def __init__(self,name,salary,role,languages):
        super().__init__(name,salary,role)
        self.languages=languages

    def printprog(self):
        return f"The programmer's name is {self.name}.\nSalary is {self.salary}.\nrole is {self.role}.\nand language is {self.languages}"


pratik=Employee("Pratik",50000,"student")
jack=Employee("jack",60000,"Super Visor")
john=Programmer("John",739,"Programmer",["Python"])
karan=Programmer("karan",342,"Programmer",["Python","cpp"])

print(karan.printprog())
print(jack.role)

# OP:-
# The programmer's name is karan.
# Salary is 342.
# role is Programmer.
# and language is ['Python', 'cpp']
# Super Visor


