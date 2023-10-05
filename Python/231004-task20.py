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

# ------------------------ Mariia ------------------------
from itertools import permutations as prm
def solution(arr):
    all_combinations = list(prm(arr, len(arr)))
    for strings in all_combinations:
        counter = 0
        for ind in range(0, len(strings) - 1):
            if strings[ind][-1] == strings[ind+1][0]:
                counter +=1
        if counter == len(arr) - 1:
            return True
    return False