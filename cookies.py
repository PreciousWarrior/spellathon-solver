import os

def is_match(pot, word_to_check, min_len):
    if len(word_to_check) < min_len:
        return False

    if len(pot) < len(word_to_check):
        return False
    word_to_check = ''.join(sorted(word_to_check))

    for char in word_to_check:
        if char not in pot:
            return False
        pot = pot.replace(char, '', 1)
        
    return True
    


def main(dictionary, min_len, pot): 
    dictionary = open(os.path.join("dictionaries", dictionary)).read().splitlines()
    pot = ''.join(sorted(pot))
    for word in dictionary:
        if is_match(pot, word, min_len):
            print(word)


pot = input("Please enter the pot of words that you would like to know a solution for: ")
pot = ''.join([i for i in pot if i.isalpha()])
pot = pot.lower()

try:
    min_len = int(input("Enter the minimum length a word can have: "))
    if min_len <= 0:
        raise ValueError()
except ValueError:
    print("Value wasn't recognized. Defaulting to '3'. ")
    min_len=3

main("lesswords.txt", min_len, pot)
