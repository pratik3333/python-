
# Python program to demonstrate working
# of map.

# Return double of n
def addition(n):
    return n + n


# We double all numbers using map()
numbers=(1,3,4,5,6,7,8,88)
s=list(map(addition,numbers))
print(s)