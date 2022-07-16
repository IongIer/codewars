# Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.


def move_zeros(lst):
    return [n for n in lst if n != 0] + [x for x in lst if x == 0]
