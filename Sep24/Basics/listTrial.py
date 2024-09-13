
courses=['history','math','physics','compsci']
print(len(courses))
print(courses[-1:])

nList=' - '.join(courses)

new_courses=nList.split(' - ')
print(nList) #separated by -
print(new_courses) #back into original form

