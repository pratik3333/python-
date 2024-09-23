

s_name=input("Enter searching name: ")
d=1
emp_file=open("employee_name.txt","r")

for emp in emp_file.readline():
    emp=emp.strip() #remove any leading/trailing white space
    if (emp.lower()==s_name.lower()):
        d=2
        break
if d==2:
    print(f"Employee found {emp}")
else:
    print("Employee not found")

emp_file.close()