#Sums of Parts
#https://www.codewars.com/kata/5ce399e0047a45001c853c2b

# ------------------------ Olesia ------------------------
def parts_sums(ls):
    total_sum = sum(ls)
    my_sum = [total_sum]

    for i in ls:
        total_sum -= i
        my_sum.append(total_sum)
    return my_sum