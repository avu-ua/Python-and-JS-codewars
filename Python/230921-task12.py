# https://www.codewars.com/kata/56121f3312baa28c8500005b

# DESCRIPTION:
# Write a function that given an array of numbers >= 0, 
# will arrange them such that they form the biggest number.

# For example:

# [1, 2, 3] --> "321" (3-2-1)
# [3, 30, 34, 5, 9] --> "9534330" (9-5-34-3-30)
# The results will be large so make sure to return a string.

# ------------------------ Olesia ------------------------
def biggest(nums):

    def custom_compare(x):
        return x * 3

    nums_str = list(map(str, nums))
    nums_str = ''.join(sorted(nums_str, key=custom_compare, reverse= True))

    if int(nums_str) > 0:
        return nums_str
    return str(0)

# ------------------------ Mariia ------------------------
import functools
def compare(x, y):
    xy = int(str(x) + str(y))
    yx = int(str(y) + str(x))
    return yx - xy

def biggest(nums):
    nums.sort(key=functools.cmp_to_key(compare))
    result = ''.join(map(str, nums))
    
    if result[0] == '0':
        return '0'    
    return result