#  Cats and shelves
#  https://www.codewars.com/kata/62c93765cef6f10030dfa92b/train/javascript

#  Mariia
def solution(start, finish):    
    return int((finish - start)/3) + (finish - start)%3

# ===============  Olesia ===============
def solution(start, finish):
    i = 0
    while start < finish:
        if finish - start == 1:
            start += 1
        elif finish - start == 2:
            start += 1
        else:
            start += 3
        i += 1
    return i

<<<<<<< HEAD

=======
# Slava
def solution(start, finish):
    return (finish - start) // 3 + (finish - start) % 3
>>>>>>> 7adb6b2e12a1e455a791f4c48e6f8ba38eedc8c4
