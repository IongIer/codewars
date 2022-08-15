# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.


def pig_it(text):
    pig = []
    for word in text.split():
        if word.isalpha():
            pig.append(word[1:] + word[0] + "ay")
        else:
            pig.append(word)
    return " ".join(pig)
