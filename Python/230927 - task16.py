#Two Sum
# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

# ------------- Slava ----------------------
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == target:
                return (i, j)

# ------------- Olesia ----------------------
def two_sum(numbers, target):
    for i in range(0, len(numbers)):
        for j in range(0, len(numbers)):
            if j == i:
                continue
            if numbers[i] + numbers[j] == target:
                return (i,j)
    return None

# ------------------------ Mariia ------------------------
def two_sum(numbers, target):
    for x in range(0, len(numbers)):
        for y in range(1, len(numbers)):
            if x == y:
                continue
            if numbers[x] + numbers[y] == target:
                return (x, y)

#Loneliest character
#https://www.codewars.com/kata/5f885fa9f130ea00207c7dc8

# -------------------- Slava --------------------------
def loneliest(strng):
    spaces = []
    for char in strng:
        if char == ' ':
            spaces.append(-1)
        else:
            left_count = 0
            right_count = 0
            for left in range(strng.index(char) - 1, -1, -1):
                if left == 0 and strng[left] == ' ':
                    left_count = 0
                    break
                else: 
                    if strng[left] == ' ':
                        left_count += 1
                    else:
                        break
            for right in range(strng.index(char) + 1, len(strng)):
                if right == len(strng) - 1 and strng[right] == ' ':
                    right_count = 0
                    break
                else:
                    if strng[right] == ' ':
                        right_count += 1
                    else:
                        break
            spaces.append(left_count + right_count)
    largest = max(spaces)
    return [strng[x] for x, y in enumerate(spaces) if y == largest]

# ------------------------ Mariia ------------------------
import re
def loneliest(strn):
    strn.lstrip()
    strn.rstrip()
    letters = [x for x in strn if x.isalpha()]
    sp = 0
    char_alone = ""
    lst_alone = [] 
    for alpha in letters:
        i = letters.index(alpha)
        if i == 0:
            spases = len(re.findall(f"{alpha}\s*", strn)[0]) - 1
            if sp < spases:
                sp = spases
                char_alone = alpha
        elif i == len(letters) - 1:
            spases = len(re.findall(f"\s*{alpha}", strn)[0]) - 1
            if sp < spases:
                sp = spases
                char_alone = alpha
        else:
            spases = len(re.findall(f"\s*{alpha}", strn)[0]) + len(re.findall(f"{alpha}\s*", strn)[0]) - 2
            if sp < spases:
                sp = spases
                char_alone = alpha
                
    for alpha in letters:
        i = letters.index(alpha)
        if i == 0:
            spases = len(re.findall(f"{alpha}\s*", strn)[0]) - 1
            if sp == spases:
                lst_alone.append(alpha)
        elif i == len(letters) - 1:
            spases = len(re.findall(f"\s*{alpha}", strn)[0]) - 1
            if sp == spases:
                lst_alone.append(alpha)
        else:
            spases = len(re.findall(f"\s*{alpha}", strn)[0]) + len(re.findall(f"{alpha}\s*", strn)[0]) - 2
            if sp == spases:
                sp = spases
                lst_alone.append(alpha)
    return list(tuple(lst_alone))

# ------------------------ Olesia ------------------------
def loneliest(strng):
    сharter_new = ""
    count_space ={}
    my_alfabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in strng:
        if i in my_alfabet:
            count_space[i] = 0
    count_of_spaces = strng.count(" ")

    key, n = '', 0
    for v in strng:
        if v != ' ':
            if key in count_space:
                count_space[key] = n
            key, n = v, 0
            continue
        else:
            n += 1
    final_count_list = {}
    prev_k, c1 = '', 0
    for k in count_space:
        if prev_k in count_space:
            c1 = count_space[prev_k]
        c2 = count_space[k]
        c = c1 + c2
        final_count_list[k] = c
        prev_k = k

    max_list = []
    max_value = max(final_count_list.values())
    for kk in final_count_list:
        if final_count_list[kk] == max_value:
            max_list.append(kk)

    return max_list
        
    