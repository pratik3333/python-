
            #Python filter function in for loop
nums=list(range(1,20))
for i in range(2,5):
    nums=list(filter(lambda x: x % i ==0, nums))
print(nums)

# OP:-
# [12]