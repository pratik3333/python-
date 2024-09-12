     #Multiple inheritance

class Employee:
    number_of_leaves=8
    def __init__(self,name,salary,role):
        self.name=name
        self.salary=salary
        self.role=role

    def printdetail(self):
        return f"The name is {self.name}.\nsalary is {self.salary}.\nrole is {self.role}"

    @classmethod
    def change_leaves(cls,new_leaves):
        cls.number_of_leaves=new_leaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

class Player:
    no_of_games=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetail(self):
        return f"The name is {self.name} and game is {self.game}"

class Coolprogrammer(Employee,Player):
    language="python"
    def printlanguage(self):
        print(self.language)

pratik=Employee("Pratik",90000,"Student")
jack=Coolprogrammer("Jack",5342,"coolprogrammer")

print(jack.printdetail())
#
# OP:-
# python
# None