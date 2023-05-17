#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    weighted_score = 0
    weighted_total = 0

    for score, weight in my_list:
        weighted_score += score * weight
        weighted_total += weight
    return weighted_score / weighted_total
