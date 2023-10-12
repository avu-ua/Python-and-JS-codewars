#Numerical Palindrome #4
#https://www.codewars.com/kata/58df8b4d010a9456140000c7

# ------------------------ Mariia ------------------------
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