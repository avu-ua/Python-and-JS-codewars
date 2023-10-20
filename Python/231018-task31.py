#Double Char
#https://www.codewars.com/kata/56b1f01c247c01db92000076/python

# ------------------------ Mariia ------------------------
def double_char(s):
    return ''.join([x*2 for x in s])

# ------------------------ Olesia ------------------------
def double_char(s):
    result = ""
    for a in s:
        result += a*2
    return result