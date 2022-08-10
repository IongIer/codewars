# In this kata you have to create all permutations of a non empty input string and remove duplicates, if present.
# This means, you have to shuffle all letters from the input in all possible orders.

from itertools import permutations as p


def permutations(iterable):
    pool = p(iterable)
    return ["".join(x) for x in set(pool)]
