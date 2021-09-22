                        #Filter() Function


"""The filter() method filters the given sequence with the help of a function that
tests each element in the sequence to be true or not.


syntax:

filter(function, sequence)

Parameters:
function: function that tests if each element of a 
sequence true or not.
sequence: sequence which needs to be filtered, it can 
be sets, lists, tuples, or containers of any iterators.
Returns:
returns an iterator that is already filtered."""




test_list=["","Hey","","","Man"]

new_list=list(filter(None,test_list))
print(new_list)