




test_list1=[1,2,3,4,5,564,6,74,437,5,434]

#even numbers
even_numbers=list(filter(lambda x:x%2 ==0,test_list1))
print(even_numbers)

#odd numbers
odd_numbers=list(filter(lambda x:x%2 != 0,test_list1))
print(odd_numbers)
# 
# OP:-
# [2, 4, 564, 6, 74, 434]
# [1, 3, 5, 437, 5]