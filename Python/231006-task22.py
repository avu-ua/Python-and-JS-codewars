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
        
# ------------------------ Mariia ------------------------
def find_missing_letter(chars):
    upper_letters = [chr(i) for i in range(65,91)]
    lower_letters = [chr(i) for i in range(97,123)]
    start_ind = upper_letters.index(chars[0]) if chars[0] in upper_letters else lower_letters.index(chars[0])
    for alpha in chars:
        if chars[0].isupper():
            if alpha != upper_letters[start_ind]:
                return upper_letters[start_ind]
        else:
            if alpha != lower_letters[start_ind]:
                return lower_letters[start_ind]
        start_ind += 1