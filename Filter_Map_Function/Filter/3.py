ages=[5, 6, 78, 23, 55, 21, 22, 20, 18, 14]

def myfunc(x):
    if x > 18 :
        return True
    return False

adults = filter(myfunc,ages)

for x in adults:
    print(x)