

#
# def add(n):
#     return n+n
# number=(12,34,564,23)
# res=map(add,number)
#
# print(list(res))


#Double all numbers using map() and lambda
import pdb

number=(12,34,564,23)
Double_number=list(map(lambda x:x+x,number))
print(Double_number)

