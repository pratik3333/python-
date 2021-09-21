"""remove() generally removes the first occurrence of empty string and
we keep iterating this process until no empty string is found in list."""

test_list=["","pratik","","kagale"]

while("" in test_list):
    test_list.remove("")

print(test_list)