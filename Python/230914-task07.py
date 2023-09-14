# Timer Decorator
# https://www.codewars.com/kata/56f84d093b164c2e490013cb

# ------------------------ Olesia ------------------------
import time
def timer(limit):
    def decorator(func):
        def inner(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            total_time = end_time - start_time
            if total_time < limit:
                return True
            return False
        return inner
    return decorator

# ------------------------ Mariia ------------------------
import time
def timer(limit):
    def calc_time(func):
        def calc(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            end = time.time()
            return end-start < limit
        return calc
    return calc_time


# Take a Number And Sum Its Digits Raised To The Consecutive Powers And ....¡Eureka!!
# https://www.codewars.com/kata/5626b561280a42ecc50000d1/train/python

# ------------------------ Olesia ------------------------
def sum_dig_pow(a, b):
    my_list = []
    for i in range(a, b+1):
        sum_numbers = 0
        for j, q in enumerate(str(i)):
            sum_numbers += int(q)**(j+1)
        if sum_numbers == i:
            my_list.append(sum_numbers)
    return my_list


# ------------------------ Mariia ------------------------
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    needed_numbers = []
    for x in range(a, b+1):
        my_iter = str(x)
        num_power_list = [int(digit)**(y+1) for y, digit in enumerate(my_iter)]
        if sum(num_power_list) == x:
            needed_numbers.append(x)
    return needed_numbers