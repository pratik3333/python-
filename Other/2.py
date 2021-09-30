
#Capitalize first and last character of each word in a string

n=input("Enter the line of string:- ")
n=n.title()
n=n.split()
string=""
for i in n:
    string +=i[:-1]+i[-1].upper()+" "
print(string)

# OP:-
# Enter the line of string:- capitalize first and last character of each word in a string
# CapitalizE FirsT AnD LasT CharacteR OF EacH WorD IN A StrinG