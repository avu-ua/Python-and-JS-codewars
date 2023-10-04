# Millipede of words
# https://www.codewars.com/kata/6344701cd748a12b99c0dbc4

# ------------------------ Olesia ------------------------

from itertools import permutations

def solution(arr):
    n = len(arr)
    result = list(permutations(range(n)))
    plural = [list(permutation) for permutation in result]
    for a in plural:
        f = 1
        for i in range(1,len(a)):
            prev_w = arr[a[i-1]]
            curr_w = arr[a[i]]
            if prev_w[-1] != curr_w[0]:
                f = 0
                break
        if f == 1:
            return True
    return False