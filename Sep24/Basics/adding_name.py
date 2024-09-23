
n=input("Enter new employee name: ")

f=open("employee_name.txt","a")

f.write(n)

f.close()