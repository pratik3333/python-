class Employee:
    raise_amount=1.04
    number_of_emps=0
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'@'+last+'.gmail.com'

        Employee.number_of_emps+=1

    def fullname(self):
        return f"{self.first},{self.last}"

    def apply_raise(self):
        self.pay=int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amount(cls,amount):
        cls.raise_amount=amount

    @classmethod
    def from_string(cls,emp_string):
        first,last,pay=emp_string.split('-')
        cls(first,last,pay)

    @staticmethod
    def is_workday(day):
        if day.weekday == 5 or day.weekday == 6:
            return True
        return False

class Developer(Employee):
    raise_amount = 1.10
    def __init__(self,first,last,pay,prog_lang,exp):
        super().__init__(first,last,pay)
        self.prog_lang=prog_lang
        self.exp=exp

class Manager(Employee):
    def __init__(self,first,last,pay,employees=None):
        super().__init__(first,last,pay)
        if employees is None:
            self.employees=[]
        else:
            self.employees=employees

    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emp(self):
        for emp in self.employees:
            print('------>>',emp.fullname())

dev1=Developer('Corey','shafer',45222,'python','3yrs')
dev2=Developer('John','sue',43222,'java','4yrs')

mgr_1=Manager('smith','jen',998009,[dev1])

print(mgr_1.email)

mgr_1.add_emp(dev2)
mgr_1.remove_emp(dev1)
mgr_1.print_emp()


# OP:-
# smith@jen.gmail.com
# ------>> John,sue