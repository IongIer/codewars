import time
import random


def add_timer(func):
    def wrapper(*args):
        start_time = time.perf_counter()
        result = func(*args)
        print(f"{func.__doc__}: {time.perf_counter() - start_time:.4f}")
        return result

    return wrapper


@add_timer
def solution0(string):
    """string concat 'aeiouAEIOU'"""
    start = ""
    for c in string:
        if c not in "aeiouAEIOU":
            start += c
    return start


@add_timer
def solution1(string):
    """join using 'aeiouAEIOU'"""
    return "".join((c for c in string if c not in "aeiouAEIOU"))


@add_timer
def solution2(string):
    """str.translate, second argument"""
    return string.translate(str.maketrans("aeiouAEIOU", "          "))


@add_timer
def solution3(string):
    """str.translate, dict string keys with empty values"""
    return string.translate(str.maketrans({k: "" for k in "aeiouAEIOU"}))


@add_timer
def solution4(string):
    """str.translate, dict string keys with None values"""
    return string.translate(str.maketrans({k: None for k in "aeiouAEIOU"}))


@add_timer
def solution5(string):
    """str.translate, dict ord keys with None values"""
    return string.translate(str.maketrans({ord(k): None for k in "aeiouAEIOU"}))


@add_timer
def solution6(string):
    """str.translate, 3rd argument"""
    remove_characters = "aeiouAEIOU"
    return string.translate(str.maketrans("", "", remove_characters))


sequence = "aeiouAEIOUzxcvbnm"
sentence = "".join(random.choice(sequence) for _ in range(8_000_000))
# sentence = "a"*(10**7) + "b"*(10**7) + "e"*(10**7)

# !!!!
# Not in order of definition
s0 = solution0(sentence)
s1 = solution1(sentence)
s3 = solution3(sentence)
s2 = solution2(sentence)
s4 = solution4(sentence)
s5 = solution5(sentence)
s6 = solution6(sentence)

print(f"s0 == s1: {s0 == s1}")
print(f"s0 == s2: {s0 == s2}")
print(f"s0 == s3: {s0 == s3}")
print(f"s0 == s4: {s0 == s4}")
print(f"s0 == s5: {s0 == s5}")
print(f"s0 == s6: {s0 == s6}")
