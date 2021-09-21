                    #Capitalize first and last character of each word in a string


s=input("Enter Line of string: ")
print(s)
s=s.title()
s=s.split()
string=""
for i in s:
    string+=i[:-1]+i[-1].upper()+" "
print(string)

