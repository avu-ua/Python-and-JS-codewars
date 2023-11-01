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