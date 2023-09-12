# Disgruntled Employee
# https://www.codewars.com/kata/541103f0a0e736c8e40011d5/python

# ---------------------- DESCRIPTION ----------------------

# Sir Bobsworth is a custodian at a local data center. As he suspected, Bobsworth recently found out he is to
# be fired on his birthday after years of pouring his soul into maintaining the facility.
# Bobsworth, however, has other plans.
# Bobsworth knows there are 1 to n switches in the breaker box of the data center. Moving from switch 1 to n, Bob
# first flips every switch off. Beginning from the first switch again, Bob then flips every 2nd switch.
# Once again starting from the first switch, Bob then flips every 3rd switch. Bob continues this pattern
# until he flips every nth switch & makes n passes.
# At the end of Bobsworth's mayhem, how many switches are turned off?
# Specifications
# Create the function off, that receives the nth switch as argument n. The function should return an ascending
# array containing all of the switch numbers that remain off after Bob completes his revenge.


# ------------------------ Slava ------------------------
def off(n):
    switches = [False] * n
    step = 2
    while step <= n:
        for index in range(step - 1, n, step):
            switches[index] = not switches[index]
        step += 1
    return [index + 1 for index, value in list(filter(lambda x: not x[1], enumerate(switches)))]

# ------------------------ Olesia ------------------------
def off(n):
    result = []
    my_list = []
    for i in range(n):
        my_list.append(0)
    a = 1
    b = 2
    for i in my_list:
        for i in range(a, n, b):
            if my_list[i] == 1:
                my_list[i] = 0
            else:
                my_list[i] = 1
        a += 1
        b += 1
    for j in range(len(my_list)):
        if my_list[j] == 0:
            result.append(j+1)
    return result

print(off(12))


# ------------------------ Mariia ------------------------
def off(n):
    switch_count = {k:1 for k in(range(1,n+1))}
    # counter = 1
    for i in range(1,n+1):
        for x in range(i,n+1,i):
            switch_count[x] *= -1
    
    indexes_of_off = [a for a in switch_count if switch_count[a]==-1]
    return indexes_of_off
