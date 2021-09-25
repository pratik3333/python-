


class Parent:
    def func1(self):
        print("This is parent class")

class Child(Parent):
    def func2(self):
        print("This is Child class")

ob=Child()
ob.func1()
ob.func2()