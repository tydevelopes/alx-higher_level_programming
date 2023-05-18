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
        elif temp.startswith("CM"):
            temp = temp.replace("CM", "", 1)
            ans += romans["CM"]
        elif temp.startswith("D"):
            temp = temp.replace("D", "", 1)
            ans += romans["D"]
        elif temp.startswith("CD"):
            temp = temp.replace("CD", "", 1)
            ans += romans["CD"]
        elif temp.startswith("C"):
            temp = temp.replace("C", "", 1)
            ans += romans["C"]
        elif temp.startswith("XC"):
            temp = temp.replace("XC", "", 1)
            ans += romans["XC"]
        elif temp.startswith("L"):
            temp = temp.replace("L", "", 1)
            ans += romans["L"]
        elif temp.startswith("XL"):
            temp = temp.replace("XL", "", 1)
            ans += romans["XL"]
        elif temp.startswith("X"):
            temp = temp.replace("X", "", 1)
            ans += romans["X"]
        elif temp.startswith("IX"):
            temp = temp.replace("IX", "", 1)
            ans += romans["IX"]
        elif temp.startswith("V"):
            temp = temp.replace("V", "", 1)
            ans += romans["V"]
        elif temp.startswith("IV"):
            temp = temp.replace("IV", "", 1)
            ans += romans["IV"]
        elif temp.startswith("I"):
            temp = temp.replace("I", "", 1)
            ans += romans["I"]

    return ans
