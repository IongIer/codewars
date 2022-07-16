# Complete the solution so that the function will break up camel casing, using a space between words.
import re


def solution(s):
    words = re.split("(?=[A-Z])", s)
    return " ".join(words)
