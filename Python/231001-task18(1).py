
#Multiplication table
#https://www.codewars.com/kata/534d2f5b5371ecf8d2000a08

# ----------------- Slava -----------------------
def multiplication_table(size):
    res = []
    first = [x + 1 for x in range(size)]
    res.append(first)
    for r in range(1, size):
        subsequent = [r + 1 if not c else (r + 1) * first[c] for c in range(size)]
        res.append(subsequent)
    return res