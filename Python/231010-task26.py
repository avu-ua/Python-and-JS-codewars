# Shortest steps to a number
# https://www.codewars.com/kata/5cd4aec6abc7260028dcd942

# ------------------------ Olesia ------------------------
def shortest_steps_to_num(num):
    if num == 1:
        return 0
    counter = 0
    n = 2
    while num > 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num -= 1
        counter += 1
    return counter
