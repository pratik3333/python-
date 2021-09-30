

#Remove empty strings from list of string

test_list=["","Hey","",'',"","Pratik"]
new_list=list(filter(None,test_list))
print(new_list)

# OP:-
# ['Hey', 'Pratik']