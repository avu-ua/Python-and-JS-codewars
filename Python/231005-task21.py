#Maximum subarray sum
#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python

# ------------------------ Mariia ------------------------
def max_sequence(arr):
    if len(arr) == 0:
        return 0
    max_sum = 0
    temp_sum = 0
    for num in arr:
        temp_sum += num
        temp_sum = max(temp_sum, 0)
        max_sum = max(max_sum, temp_sum)
    return max_sum
