# https://www.codewars.com/kata/56b7251b81290caf76000978/train/python

# As you probably know, Fibonacci sequence are the numbers in the following 
# integer sequence: 1, 1, 2, 3, 5, 8, 13... Write a method that takes the 
# index as an argument and returns last digit from fibonacci number. 
# Example: getLastDigit(15) - 610. Your method must return 0 because the last
# digit of 610 is 0. Fibonacci sequence grows very fast and value can take
# very big numbers (bigger than integer type can contain), so, please, 
# be careful with overflow.

# ------------------------ Olesia ------------------------
def get_last_digit(index):
    x, y = 0, 1
    for i in range(index-1):
        num = x + y
        x = y
        y = num
    return y % 10

# -------------------- Slava ----------------------------
def get_last_digit(index):
    if index < 2: return 1
    number_2 = 1
    number_1 = 1
    for i in range(2, index):
        number_curr = number_1 + number_2
        number_2 = number_1
        number_1 = number_curr
    return number_curr % 10

# ------------------------ Mariia ------------------------
import sys
sys.set_int_max_str_digits(0)
def get_last_digit(index):
    fib_list = [0,1]
    if index <= 1:
        return fib_list[index]
    else:
        for x in range(2,index+1):
            fib_list.append(fib_list[x-1] + fib_list[x-2])
        return int(str(fib_list[index])[-1])
    
# Покращена версія))
def get_last_digit(index):
    x,y = 1,1
    while index > 1:
        x, y, index = y, x+y, index-1
    return x%10