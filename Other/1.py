
#Find the even and odd numbers from the given list

test_list=[1,2,3,4,34,664,7,767,9787,987,4554,864534,3,756,34,43,767,98]

#even numbers

even_numbers=list(filter(lambda x:x%2 == 0,test_list))
print(f"The even numbers are: {even_numbers}")


#odd numbers
odd_numbers=list(filter(lambda x:x%2 != 0,test_list))
print(f"The odd numbers are: {odd_numbers}")
