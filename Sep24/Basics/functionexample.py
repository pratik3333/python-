

def student_info(*args,**kwargs):
    print(args)
    print(kwargs)

courses=['math','bio']
info={'name':'pratik','age':25}

student_info(*courses,**info)