#Wave Sorting
#https://www.codewars.com/kata/596f28fd9be8ebe6ec0000c1/train/python

# ----------------- Slava --------------------------
def wave_sort(a):
    a.sort(reverse=True)
    for i in range(2, len(a)):
        if not i % 2: a[i - 1], a[i] = a[i], a[i - 1]
