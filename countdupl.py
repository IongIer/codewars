# Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string.
# The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.


from collections import Counter


def duplicate_count(text):
    counts = Counter(nr for char in text.replace(" ", "") for nr in char)
    ans = sum(1 for k in counts.values() if k >= 2)
    return ans


print(duplicate_count("Indivisibilities"))
