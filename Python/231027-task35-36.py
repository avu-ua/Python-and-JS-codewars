# Refactored Greeting
# https://www.codewars.com/kata/5121303128ef4b495f000001

# ------------------------ Mariia ------------------------
class Person():
    
    def __init__ (self, name):
        self.name = name


    def greet(self, your_name):
        return f"Hello {your_name}, my name is {self.name}"

# ------------------------ Olesia ------------------------
class Person():
    def __init__(self, name):
        self.name = name

    def greet(self, your_name):
        return "Hello %s, my name is %s"% (your_name, self.name)

# Who has the most money?
# https://www.codewars.com/kata/528d36d7cc451cd7e4000339/train/python

# ------------------------ Mariia ------------------------
def most_money(students):
    if len(students) == 1:
        return students[0].name
    else:
        name = ""
        money_list = [studend.fives * 5 + studend.tens * 10 + studend.twenties * 20 for studend in students]
        if len(set(money_list)) == 1:
            return "all"
        return students[money_list.index(max(money_list))].name

# ------------------------ Olesia ------------------------
def most_money(students):
    my_list = []
    for i in students:
        money = i.fives * 5 + i.tens * 10 + i.twenties * 20
        my_list.append(money)
    if all(money == my_list[0] and len(my_list) > 1 for money in my_list):
        return "all"
    return students[my_list.index(max(my_list))].name