#Naughty or Nice
#https://www.codewars.com/kata/5662b14e0a1fb8320a00005c/train/python

# ------------------------ Olesia ------------------------
def naughty_or_nice(data):
    my_dict = {"Nice": 0, "Naughty": 0}
    for a in data:
        for b in data[a]:
            if data[a][b] == "Nice":
                my_dict["Nice"] += 1
            else:
                my_dict["Naughty"] += 1

    if my_dict["Nice"] > my_dict["Naughty"]:
        return "Nice!"
    elif my_dict["Nice"] < my_dict["Naughty"]:
        return "Naughty!"
    else:
        return "Nice!"


#Count the Digit
# https://www.codewars.com/kata/566fc12495810954b1000030/python

# ------------------------ Olesia ------------------------
def nb_dig(n, d):
    my_list = []
    for i in range(n+1):
        my_list.append(i**2)
    my_list_str = ','.join(map(str, my_list))
    n = 0
    for i in my_list_str:
        if i == str(d):
            n += 1
    return n