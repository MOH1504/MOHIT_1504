#Write a python program to find the longest words?
def find_longest_word(words):
    longest_word = []
    max_length = 0
    for word in words:
        if len(word) > max_length:
            longest_word = [word]
            max_length = len(word)
        elif len(word) == max_length:
            longest_word.append(word)
    return longest_word 

word = ["cat","dog","elephant","giraffe"] 
longest_word = find_longest_word(word)
print("the longest word are :", longest_word)             