

#Double all numbers using map() and lambda

test_list=[1,2,3,3,4,45,5,67,8,86]
new_list=list(map(lambda x:x+x,test_list))
print(new_list)