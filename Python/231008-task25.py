# https://www.codewars.com/kata/564e48ebaaad20181e000024

# One of the first chain emails I ever received was about a supposed Cambridge University study
# that suggests your brain can read words no matter what order the letters are in, as long as
# the first and last letters of each word are correct.

# Your task is to create a function that can take any string and randomly jumble the letters
# within each word while leaving the first and last letters of the word in place.

# For example,

# mixwords('Winter is coming') // returns 'Wntier is cminog' or 'Wtiner is conimg'
# mixwords('Hey, friends!') // returns 'Hey, fierdns!' or 'Hey, fernids!'
# All punctuation should remain in place
# Words smaller than 3 letters should not change
# Letters must be randomly moved (and so calling the function multiple times with the same
# string should return different values
# Parameters that are not strings should return undefined
# The tests do the following things to ensure a valid string is returned:

# Check that the string returned is not equal to the string passed (you may have to revalidate
# the solution if your function randomly returns the same string)
# Check that first and last letters of words remain in place
# Check that punctuation remains in place
# Checks string length remains the same
# Checks the function returns undefined for non-strings
# Checks that word interiors (the letters between the first and last) maintain the same letters, albeit in a different order
# Checks that letters are randomly assigned.

# ------------------------ Mariia ------------------------
import random
def sample_word(l):
    mix = ''.join(random.sample(l, len(l)))
    while mix == l:
        mix = sample_word(l)
    return mix

def mix_words(st):
    words = st.split()
    new_words = []
    for word in words:
        if len(word) <= 3 or not word[-1].isalpha() and len(word) <= 4:
            new_words.append(word)
        else:
            if word[-1].isalpha():
                new_words.append(word[0] + sample_word(word[1:-1]) + word[-1])
            else:
                new_words.append(word[0] + sample_word(word[1:-2]) + word[-2:])
    return " ".join(new_words)

# ------------------------ Olesia ------------------------
import random


def mix_words(st):
    if type(st) != str:
        return "undefined"

    result = []
    words = st.split()

    for word in words:
        word_without_special_chars = ""
        special_chars = ""
        for a in word:
            if a.isalpha():
                word_without_special_chars += a
            else:
                special_chars += a

        if len(word_without_special_chars) > 3:
            letters = list(word_without_special_chars[1:-1])
            random.shuffle(letters)
            mixed_word = word_without_special_chars[0] + ''.join(letters) + word_without_special_chars[-1] + special_chars
            result.append(mixed_word)
        else:
            result.append(word)
    return ' '.join(result)