# https://www.codewars.com/kata/64c743cb0a2a00002856ff73

# DESCRIPTION:
# Given a 2D array of some suspended blocks (represented as hastags),
# return another 2D array which shows the end result once gravity is switched on.

# Examples
# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "-", "-", "-"],
#   ["-", "#", "#", "-"]
# ]

# switch_gravity([
#   ["-", "#", "#", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "-", "-", "-"],
# ]) ➞ [
#   ["-", "-", "-", "-"],
#   ["-", "-", "#", "-"],
#   ["-", "#", "#", "-"]
# ]

# switch_gravity([
#   ["-", "#", "#", "#", "#", "-"],
#   ["#", "-", "-", "#", "#", "-"],
#   ["-", "#", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"]
# ]) ➞ [
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "-", "-", "-", "-", "-"],
#   ["-", "#", "-", "#", "#", "-"],
#   ["#", "#", "#", "#", "#", "-"]
# ]
# Notes
# Each block falls individually, meaning there are no rigid objects.
# Think about it like falling sand in Minecraft as opposed to the rigid blocks in Tetris.


# ----------------- Slava ------------------------
def switch_gravity(lst):
    for column in range(len(lst[0])):
        blocks = 0
        for row in range(len(lst)):
            if lst[row][column] == '#': blocks += 1
        for row in range(len(lst)):
            lst[row][column] = '-' if row < len(lst) - blocks else '#'
    return lst

# ----------------- Olesia ------------------------
def switch_gravity(my_list):
    r_list = []
    def reverse(my_list):
        new_list = []
        n = len(my_list[0])
        for i in range(n):
            temp_list = []
            for a in my_list:
                temp_list.append(a[i])
            new_list.append(temp_list)
        return new_list

    new_list = reverse(my_list)

    for item in new_list:
        temp_r_list = []
        for v in item:
            if v == "-":
                temp_r_list.insert(0, v)
            else:
                temp_r_list.append("#")
        r_list.append(temp_r_list)
    return reverse(r_list)

# ------------------------ Mariia ------------------------
def switch_gravity(lst):
    rows, cols = len(lst), len(lst[0])
    
    blocks_in_column = [sum(lst[row][col] == '#' for row in range(rows)) for col in range(cols)]
    
    result = [['-' for _ in range(cols)] for _ in range(rows)]
    for col, num_blocks in enumerate(blocks_in_column):
        for row in range(rows - num_blocks, rows):
            result[row][col] = '#'
    
    return result    