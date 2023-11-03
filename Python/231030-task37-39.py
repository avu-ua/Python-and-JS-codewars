# Merging sorted integer arrays (without duplicates)
# https://www.codewars.com/kata/573f5c61e7752709df0005d2

# ------------------------ Olesia ------------------------
def merge_arrays(first, second):
    my_list = first + second
    my_list = list(set(my_list))
    while True:
        f = 1
        for i in range(1, len(my_list)):
            prev = my_list[i - 1]
            next = my_list[i]
            if next < prev:
                my_list[i - 1], my_list[i] = next, prev
                f = 0
        if f == 1:
            break
    return my_list
print(merge_arrays([2, 4, 8], [2, 4, 6]))

# ------------------------ Mariia ------------------------
def merge_arrays(first, second): 
    return sorted(list(set(first+second)))

#task38
# Count by X
#https://www.codewars.com/kata/5513795bd3fafb56c200049e/python

# ------------------------ Mariia ------------------------
def count_by(x,n):
    lst = []
    for y in range(1,n+1):
        lst.append(x*y)
    return lst

#task39
#altERnaTIng cAsE <=> ALTerNAtiNG CaSe
#https://www.codewars.com/kata/56efc695740d30f963000557/python

# ------------------------ Mariia ------------------------
def to_alternating_case(string):
    st = ""
    for x in string:
        if x.isalpha():
            if x.isupper():
                st += x.lower()
            else:
                st += x.upper()
        else:
            st += x
    return st

# Потім я дізналась про існування функції swapcase() :)
def to_alternating_case(string):
    return string.swapcase()