#!/usr/bin/python
import os
import random

#
# presentation
#


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#
# logic
#


def convert_to_camel(string):
    # "abc cde" -> "AbcCde"
    res = ""
    for word in string.split():
        res += word.capitalize()
    return res


def derive_ability(score):
    return score / 2 - 5


# roll_the_dices
def calc_parcel(parcel):
    total = 0
    if "d" in parcel:
        n_of_dices, type_of_dice = parcel.split("d")
        for dice in range(0, int(n_of_dices)):
            total += random.randint(1, int(type_of_dice))
    else:
        total += int(parcel)
    return total


def update_total(total, parcel, operation):
    parcel_result = calc_parcel(parcel)
    to_exec = "total %s= %s" % (operation, parcel_result)
    exec(to_exec)
    return total


def roll_the_dices(dices):
    dices = str(dices).replace(" ", "")
    total = 0
    parcel = ""
    if dices[0] == "-":
        operation = "-"
        dices = dices[1:]
    else:
        operation = "+"
    for i, x in enumerate(dices):
        # print "x:%s i:%s" % (x, i)
        if x in ["+", "-"]:
            total = update_total(total, parcel, operation)
            operation = x
            parcel = ""
        else:
            parcel += x
    total = update_total(total, parcel, operation)
    return total

#
# END
#
