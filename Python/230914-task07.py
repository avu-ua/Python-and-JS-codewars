# Timer Decorator
# https://www.codewars.com/kata/56f84d093b164c2e490013cb


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
