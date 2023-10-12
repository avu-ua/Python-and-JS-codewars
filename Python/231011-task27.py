#Numerical Palindrome #4
#https://www.codewars.com/kata/58df8b4d010a9456140000c7

# ------------------------ Mariia ------------------------
# Домучила її тільки з чатом GPT((  Одразу не додумалась в циклі зменшувати і збільшувати на 1
def is_palindrome(n):
    return str(n) == str(n)[::-1]

def palindrome(num):
    if not isinstance(num, int) or num < 0:
        return "Not valid"
    
    if num < 15:
        return 11
    
    lower_palindrome = num
    higher_palindrome = num
    while not (is_palindrome(lower_palindrome) or is_palindrome(higher_palindrome)):
        lower_palindrome -= 1
        higher_palindrome += 1
    
    return higher_palindrome if is_palindrome(higher_palindrome) else lower_palindrome

# ------------------------ Olesia ------------------------

def palindrome(num):
    if type(num) != int:
        return "Not valid"
    if num < 0:
        return "Not valid"
    if len(str(num)) == 1:
        return 11

    small_palindrome = 0
    big_palindrome = 0

    num1 = num

    while str(num1) != small_palindrome:
        num1 = num1 - 1
        small_palindrome = str(num1)[::-1]

    while str(num1) != big_palindrome:
        num1 = num1 + 1
        big_palindrome = str(num1)[::-1]

    diff1 = abs(num - int(small_palindrome))
    diff2 = abs(num - int(big_palindrome))

    if diff1 < diff2:
        return int(small_palindrome)
    else:
        return int(big_palindrome)