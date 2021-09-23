

#Capitalize the first and last letters

n='nitin'
n=n.title()
n=n.split()
string=""
for i in n:
    string+=i[:-1]+i[-1].upper()+" "
print(string)

# n=input("Enter Line of string:")
# n=n.title()
# n=n.split()
# string=" "
# for i in n:
#     string+=i[:-1]+i[-1].upper()+" "
# print(string)