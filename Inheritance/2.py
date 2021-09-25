class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        self.email=fname+lname+'@gmail.com'

    def printname(self):
        print(self.firstname,self.lastname)

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

x=Student("Mike","joe",2021)
print(x.graduationyear)
print(x.email)

# OP:-
# 2021
# Mikejoe@gmail.com
