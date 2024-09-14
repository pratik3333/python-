

for i in range(4):
    for j in range(7):
        if ((j>=3-i) and (j<=3+i)):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()