# Highest Scoring Word
# https://www.codewars.com/kata/57eb8fcdf670e99d9b000272/train/python

# ---------------------- DESCRIPTION ----------------------

# Given a string of words, you need to find the highest scoring word.
# Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.
# For example, the score of abad is 8 (1 + 2 + 1 + 4).
# You need to return the highest scoring word as a string.
# If two words score the same, return the word that appears earliest in the original string.
# All letters will be lowercase and all inputs will be valid.

# ------------------------ Olesia ------------------------
def high(x):
    list_sum_of_words = {}
    input_words = x.split()
    my_alphabet = "abcdefghijklmnopqrstuvwxyz"
    my_alphabet_dict = {}
    for i in my_alphabet:
        my_alphabet_dict[i] = my_alphabet.index(i)+1
    for i in input_words:
        result = 0
        for j in i:
            if j in my_alphabet_dict:
                result += my_alphabet_dict[j]
        list_sum_of_words[i] = result
        max_value = max(list_sum_of_words, key=list_sum_of_words.get)
    return max_value

print(high('up taxi aaaaaaaaaaaaa'))

# ------------------------ Mariia ------------------------
import functools

def high(x):
    words_array = (x.lower()).split()
    counter = functools.reduce(lambda x, y: x +ord(y)-ord("a")+1 , words_array[0], 0)
    bigger_word = words_array[0]
    for i in words_array:
        if functools.reduce(lambda x, y: x +ord(y)-ord("a")+1 , i, 0) > counter:
            counter = functools.reduce(lambda x, y: x +ord(y)-ord("a")+1 , i, 0)
            bigger_word = i
    return bigger_word


# --------------- Slava ---------------------------
def high(x):
    values = [sum(ord(i) - 96 for i in word) for word in x.split()]
    return x.split()[values.index(max(values))]