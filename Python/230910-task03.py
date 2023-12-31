#Duplicate Encoder
#https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python

# ---------------------- DESCRIPTION ----------------------
# The goal of this exercise is to convert a string to a new string where each character
# in the new string is "(" if that character appears only once in the original string, or ")"
# if that character appears more than once in the original string. Ignore capitalization
# when determining if a character is a duplicate.

# ===============  Olesia ===============
def duplicate_encode(word):
    small_word = word.lower()
    count_word = {}
    my_str = ""
    for i, j in enumerate(small_word):
        count_word[j] = small_word.count(j.lower())
        if count_word[j] > 1:
            my_str += ")"
        else:
            my_str += "("
    return my_str

print(duplicate_encode("xwsyZDbr@GaRxA! G@RSs"))

# ===============  Mariia ===============
def duplicate_encode(word):
    lower_word = word.lower()
    result = ''
    for i in lower_word:
        counter = lower_word.count(i)
        if counter > 1:
            result +=')'
        else:
            result +='('
    return result

# ===============  Slava ===============
def duplicate_encode(word):
    new_string = ''
    for char in word.lower():
        new_string += '(' if word.lower().count(char) == 1 else ')'
    return new_string

# ===============  Yuliia ===============
def duplicate_encode(word):
    new_word = word.lower()
    result = []
    for i in new_word:
        count_letter = new_word.count(i)
        if count_letter == 1:
            result.append("(")
        else:
            result.append(")")
    result_string = "".join(result)
    return result_string
