                  #Using join() + split()
"""Combining both the join() and split() operations, this task can also be 
achieved.We first join all the strings so that empty space is removed, and then 
split it back to list so that new list made now has no empty string."""

test_list=["","pratik","","","Thank You"]

#Using Join() + Split() to
#perform removal
new_list=" ".join(test_list).split()
print(new_list)