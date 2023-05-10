# Write a Python program to count the frequency of words in a file?
from collections import couter
with open ("example10.txt",'r') as file:
    coutents = file.read()
    words = coutents.split()
    word_counts = coutents(words)
    for word, count in word_counts.items():
        print(f'{word}: {count}')