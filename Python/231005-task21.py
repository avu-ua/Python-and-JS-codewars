#Maximum subarray sum
#https://www.codewars.com/kata/54521e9ec8e60bc4de000d6c/train/python
# ------------------------ Olesia ------------------------
def max_sequence(arr):
    if not arr:
        return 0
    if all(num < 0 for num in arr):
        return 0
    max_num = 0
    result = []
    for num in arr:
        max_num = max(num, max_num + num)
        result.append(max_num)
    return max(result)