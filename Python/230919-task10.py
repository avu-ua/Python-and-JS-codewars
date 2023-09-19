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