# Given an array of integers, find the one that appears an odd number of times.

# There will always be only one integer that appears an odd number of times.

#Bad solution
# from collections import Counter


# def find_it(seq):
#     count = Counter(seq)
#     for x in count:
#         if count[x] % 2 != 0:
#             return x
from functools import reduce
import operator

def find_it(seq):
    return reduce(operator.xor , seq)

print(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))