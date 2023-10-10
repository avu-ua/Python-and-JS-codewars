#Wave Sorting
#https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/python

# ----------------- Slava --------------------------
def wave_sort(a):
    a.sort(reverse=True)
    for i in range(2, len(a)):
        if not i % 2: a[i - 1], a[i] = a[i], a[i - 1]

# ------------------------ Mariia ------------------------
def wave_sort(a):
    a.sort()
    for x in range (0, len(a) - 1, 2):
        a[x], a[x+1] = a[x+1], a[x]

# ------------------------ Olesia ------------------------
def wave_sort(a):
    a.sort()
    for i in range(0,(len(a)-1),2):
        a[i], a[i + 1] = a[i + 1], a[i]