# https://www.codewars.com/kata/592645498270ccd7950000b4

# Task
# John is a typist. He has a habit of typing: he never use 
# the Shift key to switch case, just using only Caps Lock.

# Given a string s. Your task is to count how many times the 
# keyboard has been tapped by John.

# You can assume that, at the beginning the Caps Lock light is not lit.

# Input/Output: 
# [input] 
# - string s - a non-empty string. It contains only English letters(uppercase or lowercase).
# - 1 ≤ s.length ≤ 10000
# [output] an integer - the number of times John tapped the keyboard.

# Examples:
# 1) For s = "a", the output should be 1: John hit button a.
# 2) For s = "aa", the output should be 2 - John hit button a, a.
# 3) For s = "A", the output should be 2 - John hit button Caps Lock, A.
# 4) For s = "Aa", the output should be 4 - John hit button Caps Lock, A, Caps Lock, a.

# --------------- Slava -------------------------

# ----- SOLUTION 1 - Easy to understand ------------
def typist(s):
    if len(s) == 1:
        return 1 if s.islower() else 2
    count = len(s) if s[0].islower() else len(s) + 1
    for i in range(len(s) - 1):
        if s[i].islower() != s[i+1].islower(): count += 1
    return count

# ----- SOLUTION 2 - One-liner but confusing ------------
def typist(s):
    return sum(list(map(lambda x: 1 if (x == 0 and s[x].isupper()) or (len(s) > 1 and x > 0 and s[x].islower() != s[x-1].islower()) else 0, dict(enumerate(s))))) + len(s)