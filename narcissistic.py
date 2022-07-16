# A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the number of digits in a given base.
# In this Kata, we will restrict ourselves to decimal (base 10).


def narcissistic(value):
    digits = [*map(int, str(value))]
    powered = [n ** len(str(value)) for n in digits]
    return sum(powered) == value
