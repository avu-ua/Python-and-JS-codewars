#Two Sum
# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python

# ------------- Slava ----------------------
def two_sum(numbers, target):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i != j and numbers[i] + numbers[j] == target:
                return (i, j)

#Loneliest character
#https://www.codewars.com/kata/5f885fa9f130ea00207c7dc8

# -------------------- Slava --------------------------
def loneliest(strng):
    spaces = []
    for char in strng:
        if char == ' ':
            spaces.append(-1)
        else:
            left_count = 0
            right_count = 0
            for left in range(strng.index(char) - 1, -1, -1):
                if left == 0 and strng[left] == ' ':
                    left_count = 0
                    break
                else: 
                    if strng[left] == ' ':
                        left_count += 1
                    else:
                        break
            for right in range(strng.index(char) + 1, len(strng)):
                if right == len(strng) - 1 and strng[right] == ' ':
                    right_count = 0
                    break
                else:
                    if strng[right] == ' ':
                        right_count += 1
                    else:
                        break
            spaces.append(left_count + right_count)
    largest = max(spaces)
    return [strng[x] for x, y in enumerate(spaces) if y == largest]