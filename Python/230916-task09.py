#WeIrD StRiNg CaSe
#https://www.codewars.com/kata/52b757663a95b11b3d00062d/train/python


# ------------------------ Mariia ------------------------
def to_weird_case(words):
    words_list = words.split()
    weird_str = []
    for x in words_list:
        word_iter = list(x)
        for y in range(0, len(word_iter)):
            if y%2 == 0 or y == 0:
                word_iter[y] = word_iter[y].upper()
            else:
                word_iter[y] = word_iter[y].lower()
        weird_str.append("".join(word_iter))
    return " ".join(weird_str)

# ------------------------ Olesia ------------------------
def to_weird_case(words):
    my_list = words.split()
    sort_words = []
    for i in my_list:
        sort_word = ""
        for a, b in enumerate(i):
            if a % 2 == 0:
                sort_word += b.upper()
            else:
                sort_word += b.lower()
        sort_words.append(sort_word)
    return " ".join(sort_words)

# ---------------------- Slava -----------------------------
def to_weird_case(words):
    return ' '.join(''.join(word[x].upper() if x % 2 == 0 else word[x].lower() for x in range(0, len(word))) for word in words.split())

#Build a pile of Cubes
#https://www.codewars.com/kata/5592e3bd57b64d00f3000047/train/python

# ------------------------ Olesia ------------------------
def find_nb(m):
    sum = 0
    x = 1
    n = 0
    while sum < m:
        sum += x**3
        x += 1
        n += 1
    if sum == m:
        return n
    else:
        return -1

