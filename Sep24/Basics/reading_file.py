
emp_file=open("employee_name.txt","r")

search_emp=input("Enter search name: ")
# print(search_emp)
a=1

for employee in emp_file.readlines():
    employee=employee.strip() # Remove any leading/trailing whitespaces (including newlines)
    if (search_emp.lower() == employee.lower()):
        a=2
        break
    # print(employee)
if a==1:
    print("not found")
elif a==2:
    print(f"Found Employee {employee}")

emp_file.close()