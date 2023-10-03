# Find All the Possible Numbers Multiple of 3 with the Digits of a Positive Integer.
# https://www.codewars.com/kata/5828b9455421a4a4e8000007

# ------------------------ Olesia ------------------------щоб пройшло на кодварс треба декілька разів тест запустити :)
import itertools
def find_mult_3(num):
    list_combination = set()
    num1 = str(num)
    for item in range(1, len(num1) + 1):
        for a in itertools.permutations(num1, item):
            num = int("".join(a))
            if num % 3 == 0 and num != 0:
                list_combination.add(num)
    return [len(list_combination), max(list_combination)]