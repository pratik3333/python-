class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
        #self.email=fname+lname+'@gmail.com'

    def printname(self):
        print(self.firstname,self.lastname)


    @property
    def email(self):
        if self.firstname==None:
            return 'Email not set'
        else:
            return self.firstname+'.'+self.lastname+'123@gmail.com'

class Student(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year

x=Student("Mike","joe",2021)
print(x.graduationyear)
print(x.email)

# OP:-
# 2021
# Mike.joe123@gmail.com
