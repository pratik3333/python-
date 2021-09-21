                              #Using List Comprehension

"""More concise and better approach to remove all the empty strings, it just checks
if the string is not empty and re-makes the list with all strings that are not empty."""



test_list=["","Hey","","","Pratik"]

new_list=[i for i in test_list if i]
print(new_list)