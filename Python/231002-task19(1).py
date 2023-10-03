# Find The Parity Outlier
# https://www.codewars.com/kata/5526fc09a1bbd946250002dc

# ------------------------ Olesia ------------------------
def find_outlier(integers):
    odd_list = []
    even_list = []
    for i in integers:
        if i % 2 == 1:
            odd_list.append(i)
        else:
            even_list.append(i)
    if len(odd_list) < len(even_list):
        return odd_list[0]
    return even_list[0]

# ------------------------ Mariia ------------------------
def find_outlier(integers):
    even = [x for x in integers if x%2 == 0]
    odd = [x for x in integers if x%2 == 1]
    return even[0] if len(even) == 1 else odd[0]