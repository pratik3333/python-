"""In Python, string is an immutable sequence data type.
It is the sequence of Unicode characters wrapped inside single, double, or triple quotes."""
#
# str="Geeksforgeeks is fun"
#
# n=4
# modified_str=''
# for char in range(0,len(str)):
#     if(char != n):
#        modified_str +=str[char]
#
# print(modified_str)

test_list=["","","pratik"]
# new_list=list(filter(None,test_list))
# print(f"The modified list is {new_list}")

new_list=list(filter(lambda x:x, test_list))
print(new_list)


s='nratim'
s=s.title()
s=s.split()
string=""
for i in s:
    string+=i[:-1]+i[-1].upper()+""
print(s)

s=input("Enter line of string:")
s=s.title()
s=s.split()
string=""
for i in s:
    string+=i[:-1]+i[-1].upper()+" "
print(string)


