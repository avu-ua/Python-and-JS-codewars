# Simple Pig Latin
# https://www.codewars.com/kata/520b9d2ad5c005041100000f/train/python


# ------------------------ Mariia ------------------------
def pig_it(text):
    lst_text = list(text.split())
    counter = 0
    for x in lst_text:
        if x[-1].isalpha():
            lst_text[counter] = x[1:] + x[0] + "ay"  
        elif x[-1].isalpha() == False:
            continue
        else:
            lst_text[counter] = x[1:-1] + x[0] + "ay" + x[-1]
        counter +=1
    return " ".join(lst_text)

# ------------------------ Olesia ------------------------
def pig_it(text):
    special_characters = '"!@#$%^&*()-+?_=,<>/"'
    my_list = []
    for i in text.split():
        if i not in special_characters:
            a = i[0]
            b = i[1::]
            y = b + a + "ay"
            my_list.append(y)

    if text[-1] in special_characters:
        return " ".join(my_list) + " " + text[-1]
    else:
        return " ".join(my_list)