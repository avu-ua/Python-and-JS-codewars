# Find the missing letter
#https://www.codewars.com/kata/5839edaa6754d6fec10000a2

# ------------ Slava --------------------

def find_missing_letter(chars):
    for i in range(len(chars) - 1):
        if (ord(chars[i+1]) - ord(chars[i]) > 1): return chr(ord(chars[i]) + 1)
    return chr(ord(chars[-1]) + 1)

# ------------ Olesia --------------------
def find_missing_letter(chars):
    chars_lower = [letter.lower() for letter in chars]
    my_alfabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    for i in range(my_alfabet.index(chars_lower[0]), my_alfabet.index(chars_lower[-1])):
        if my_alfabet[i] not in chars_lower:
            if chars[0].lower() in chars:
                return my_alfabet[i]
            return my_alfabet[i].upper()