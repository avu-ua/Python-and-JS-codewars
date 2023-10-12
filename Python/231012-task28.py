# A Letter's Best Friend
# https://www.codewars.com/kata/64fc03a318692c1333ebc04c

# ------------------------ Mariia ------------------------
def best_friend(txt, a, b):
    return True if txt.count(a+b) == txt.count(a) else False