# String incrementer
# https://www.codewars.com/kata/54a91a4883a7de5d7800009c/train/python

# Ресурси, що допоможуть з regexp для цієї задачі:
# https://www.w3schools.com/python/python_regex.asp
# https://regex101.com/

# ------------------------ Mariia ------------------------
import re
def increment_string(strng):
    num_str = re.findall("\d*$", strng)[0]
    new_str = ""
    if not num_str:
        new_str = strng + "1"
    else:
        num = str(int(num_str) + 1)
        if len(num) >= len(num_str):
            new_str = strng[0:(len(strng) - len(num_str))] + num
        else:
            new_str = strng[0:(len(strng) - len(num_str))] +"0"*(len(strng) - len(strng[0:(len(strng) - len(num_str))]) - len(num)) + num
    return new_str


# ------------------ Slava ----------------------------
def increment_string(strng):
    for i in range(len(strng)):
        if strng[i:].isnumeric():
            dig_fragment = strng[i:]
            digit = int(dig_fragment)
            return strng[0 : i] + strng[i : i + len(dig_fragment) - len(str(digit + 1))] + str(digit + 1)
    return strng + '1'

# ------------------------ Olesia ------------------------
def increment_string(strng):
    my_digit = []
    for i in strng[:: -1]:
        if i.isdigit():
            my_digit.append(i)
        else:
            break
    if not my_digit:
        return strng + '1'
    num = int(''.join(my_digit[::-1])) + 1
    return strng[0:-len(my_digit)] + str(num).zfill(len(my_digit))