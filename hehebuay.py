import os


def possible_occurrence(letters, to_check, min_len=4):
    if len(to_check) < min_len:
        return False
    for character in to_check:
        try:
            letters.index(character)
            letters = letters.replace(character, '')
        except ValueError:
            return False
    return True


word = input("Enter all the letters in the puzzle in any order (including the central letter) : ").lower()
central_letter = input("Enter the central letter: ").lower()

file = open(os.path.join("dictionaries", "words.txt"), "r")
dictionary = file.readlines()
file.close()

print("Possible Solutions: ")
for dic_word in dictionary:
    editable_word = word
    dic_word = dic_word.replace('\n', '')
    if central_letter in dic_word:
        if possible_occurrence(word, dic_word):
            print(dic_word)
