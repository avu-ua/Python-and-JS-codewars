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
        num = (x + y) % 10
        x = y
        y = num
    return y % 10