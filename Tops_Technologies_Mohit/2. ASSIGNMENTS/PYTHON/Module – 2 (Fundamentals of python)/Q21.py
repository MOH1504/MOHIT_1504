#Write a Python function that takes a list of words and returns the length of the longest one.

def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts

print( word_count('Tops technology'))