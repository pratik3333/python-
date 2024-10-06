
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

    def avg(self):
        sum=0
        for val in self.marks:
            sum +=val
        print(f"average is {sum/3}")

s1=Student("pratik",[35,45,55])
s1.avg()
