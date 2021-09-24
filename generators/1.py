


def topten():

    n=5

    while n<=10:
        sq=n*n
        yield sq
        n +=1


values=topten()

for i in values:
    print(i)

# OP:-
# 25
# 36
# 49
# 64
# 81
# 100