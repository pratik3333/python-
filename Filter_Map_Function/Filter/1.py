
    #Finding the even and odd numbers from the given list

number=[23,54,44,65,77,87,99,78,66,88,44]

even_number=list(filter(lambda x : x%2 ==0,number))
print(even_number)

odd_number=list(filter(lambda x : x%2 !=0,number))
print(odd_number)



# #OP:-
# [54, 44, 78, 66, 88, 44]
# [23, 65, 77, 87, 99]
