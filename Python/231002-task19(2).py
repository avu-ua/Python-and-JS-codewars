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

# ------------------------ Mariia ------------------------
# Ось рішення, яке я написала спочатку. Воно проходить тести, але займає багато часу, тому всі тести воно не встигає проходити((
    
# import itertools
# def find_mult_3(number):
#     all_numbers = []
#     for num in range(1, len(str(number)) + 1):
#         all_numbers += [x for x in list(itertools.permutations(str(number), num))]
    
#     all_int = [int(''.join(x)) for x in all_numbers if int(''.join(x)) % 3 == 0 if int(''.join(x)) != 0]
#     num_3 = sorted(list(set(all_int))) 
    
#     return [len(num_3), num_3[-1]]

# А це вже я переробила своє рішення за прикладом Олесі, бо замучилась)) Воно проходить всі тести)
import itertools
def find_mult_3(number):
    all_numbers = []
    for num in range(1, len(str(number))+1):
        for three in itertools.permutations(str(number), num):
            item = int(''.join(three))
            if item % 3 == 0 and item != 0:
                all_numbers.append(item)
    num_3 = sorted(list(set(all_numbers)))
    return [len(num_3), num_3[-1]]