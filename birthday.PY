#given the number of people in the room, calculate the probability that any two people in that 
# room have the same birthday, assuming we have 365 days in a year. (no leap years) Return the probability
#  rounded off to two decimal points.
# def calculate_probability(n):
#     return probability
# Hint: In order to calculate the probability, you might find it useful to use the probability
#  that NO ONE shares the same birthday in the room:
# 365! / ((365-n)! * 365^n)
# The ! sign above denotes the mathematical notation factorial.
#  eg. 10! = 10 x 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1
# The math module in Python has a built-in function for factorials which you can easily call. 
# As a challenge you can also attempt the question without using the built-in factorial function.
# Here's a link on how to calculate birthday probability.

def calculate_probability(n):
    from math import factorial as f
    return round((1-f(365)/(f(365-n)*(365**n))), 2)

print(calculate_probability(4))