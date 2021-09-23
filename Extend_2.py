

#Add Any Iterable
#The extend() method does not have to append lists, you can add any iterable object
# (tuples, sets, dictionaries etc.).

#Add elements of a tuple to a list:

this_list=["hey","man","how"]
this_tuple=("jack","Reacher","Tom")
this_list.extend(this_tuple)
print(this_list)

# OP:-
# ['hey', 'man', 'how', 'jack', 'Reacher', 'Tom']