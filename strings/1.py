"""In Python, string is an immutable sequence data type.
It is the sequence of Unicode characters wrapped inside single, double, or triple quotes."""

str="Geeksforgeeks is fun"

n=4
modified_str=''
for char in range(0,len(str)):
    if(char != n):
       modified_str +=str[char]

print(modified_str)
