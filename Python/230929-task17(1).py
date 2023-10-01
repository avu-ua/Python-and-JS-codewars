# https://www.codewars.com/kata/59752e1f064d1261cb0000ec

# Story
# Due to lack of maintenance the minute-hand has fallen off Town Hall clock face.

# And because the local council has lost most of our tax money to an elaborate email
# scam there are no funds to fix the clock properly.

# Instead, they are asking for volunteer programmers to write some code that tell
# the time by only looking at the remaining hour-hand!

# What a bunch of cheapskates!

# Can you do it?

# Kata
# Given the angle (in degrees) of the hour-hand, return the time in 12 hour HH:MM format.
# Round down to the nearest minute.

# Examples
# 12:00 = 0 degrees
# 03:00 = 90 degrees
# 06:00 = 180 degrees
# 09:00 = 270 degrees
# 12:00 = 360 degrees

# Notes
# 0 <= angle <= 360

# Do not make any AM or PM assumptions for the HH:MM result.
# They are indistinguishable for this Kata.

# 3 o'clock is 03:00, not 15:00
# 7 minutes past midnight is 12:07
# 7 minutes past noon is also 12:07

# ----------------- Slava ------------------------
import math
def what_time_is_it(angle):
    hours = math.floor(angle / 30) if math.floor(angle / 30) else 12
    minutes = math.floor(60 * ((angle - math.floor(angle / 30) * 30) / 30))
    return "{:02d}:{:02d}".format(hours, minutes)

print(what_time_is_it(359))

# ------------------------ Mariia ------------------------
from math import floor
def what_time_is_it(angle):
    hours = str(int(angle // 30))
    minutes = str(floor((angle % 30) * 2))
    if hours == "0":
        hours = "12"
    if len(hours) == 1:
        hours = "0" + hours
    if len(minutes) == 1:
        minutes = "0" + minutes
    return hours + ":" + minutes

# ------------------------ Olesia ------------------------
import math
def what_time_is_it(angle):
    time_mm = angle * 2
    time_hh = int(time_mm/60)
    time_m = int(math.floor(time_mm - (time_hh * 60)))
    time_h_str = str(time_hh).zfill(2)
    time_m_str = str(time_m).zfill(2)
    if angle < 30:
        return "12" + ":" + time_m_str
    return time_h_str + ":" + time_m_str