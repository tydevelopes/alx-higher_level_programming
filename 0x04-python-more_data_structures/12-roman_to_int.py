#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    if not roman_string or (not type(roman_string) is str):
        return 0
    ans = 0
    temp = roman_string.upper()

    while temp:
        if temp.startswith("M"):
            temp = temp.replace("M", "", 1)
            ans += romans["M"]
        elif temp.startwith("CM"):
            temp = temp.replace("CM", "", 1)
            ans += romans["CM"]
        elif temp.startwith("D"):
            temp = temp.replace("D", "", 1)
            ans += romans["D"]
        elif temp.startwith("CD"):
            temp = temp.replace("CD", "", 1)
            ans += romans["CD"]
        elif temp.startwith("C"):
            temp = temp.replace("C", "", 1)
            ans += romans["C"]
        elif temp.startwith("XC"):
            temp = temp.replace("XC", "", 1)
            ans += romans["XC"]
        elif temp.startwith("L"):
            temp = temp.replace("L", "", 1)
            ans += romans["L"]
        elif temp.startwith("XL"):
            temp = temp.replace("XL", "", 1)
            ans += romans["XL"]
        elif temp.startwith("X"):
            temp = temp.replace("X", "", 1)
            ans += romans["X"]
        elif temp.startwith("IX"):
            temp = temp.replace("IX", "", 1)
            ans += romans["IX"]
        elif temp.startwith("V"):
            temp = temp.replace("V", "", 1)
            ans += romans["V"]
        elif temp.startwith("IV"):
            temp = temp.replace("IV", "", 1)
            ans += romans["IV"]
        elif temp.startwith("I"):
            temp = temp.replace("I", "", 1)
            ans += romans["I"]

    return ans
