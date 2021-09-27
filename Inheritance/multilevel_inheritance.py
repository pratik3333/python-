          #Multilevel inheritance


class Dad:
    backetball=1

class Son(Dad):
    Dance=1
    def isdance(self):
        return f"Yes i dance {self.Dance} number of times."

class Grandson(Son):
    Dance = 6
    backetball=78

    def isdance(self):
        return f"Jackson yeah! yes i dance very awesomely {self.Dance} number of times"

class Grandson(Son):
    Dance = 6
    backetball=78

    def isdance(self):
        return f"Jackson yeah! yes i dance very awesomely {self.Dance} number of times"



darry=Dad
larry=Son
harry=Grandson

print(darry.backetball)
print(larry.backetball)
print(harry.backetball)

print(harry.isdance(Son))
print(larry.isdance(Grandson))

# OP:-
# 1
# 1
# 78
# Jackson yeah! yes i dance very awesomely 1 number of times
# Yes i dance 6 number of times.
