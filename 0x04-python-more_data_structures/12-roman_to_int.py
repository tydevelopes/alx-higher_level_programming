#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40,
              'L': 50, 'XC': 90, 'C': 100, 'CD': 400,
              'D': 500, 'CM': 900, 'M': 1000}
    if not roman_string or (not type(roman_string) is str):
        return 0
    ans = 0
    temp = roman_string.upper()

    while (temp):
        for key, value in romans.items():
            if temp.startswith(key):
                temp = temp.replace(key, "", 1)
                ans += value
    return ans
