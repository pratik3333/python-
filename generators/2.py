



def gen(n):
    for i in range(n):
        yield i


g=gen(5)

# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

for i in g:
    print(i)

