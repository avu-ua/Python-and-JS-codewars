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
