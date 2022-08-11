# better than my solution and important not to make the set inside the list comp as it does it every loop


def array_diff(a, b):
    set_b = set(b)
    return [i for i in a if i not in set_b]
