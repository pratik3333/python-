def fun(variable):
    letters=['a','e','i','o','u']
    if (variable in letters):
        return True
    else:
        return False


sequence=['a','d','g','r','e','g','k','a','i']

filtered=list(filter(fun,sequence))

print('Filtered letters are:')
for s in filtered:
    print(s)

# Op:-
# Filtered letters are:
# a
# e
# a
# i