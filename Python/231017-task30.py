# Neutralisation
# https://www.codewars.com/kata/65128732b5aff40032a3d8f0

# ------------------------ Mariia ------------------------
def neutralise(s1, s2):
    return "".join([s1[x] if s1[x]==s2[x] else "0" for x in range(0, len(s1))])