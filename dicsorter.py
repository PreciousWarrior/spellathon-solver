import os

file = open("dictionaries/lesswords.txt", "r+")
dictionary = file.read().splitlines()

dictionary.sort()
dictionary.sort(key=len, reverse=True)

file.truncate(0)
for word in dictionary:
    file.write(word)
    file.write("\n")