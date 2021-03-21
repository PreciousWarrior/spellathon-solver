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
        pot = pot.replace(char, '')
        
    return True
    


def main(dictionary, min_len, pot): 
    dictionary = open(os.path.join("dictionaries", dictionary)).read().splitlines()
    pot = ''.join(sorted(pot))
    for word in dictionary:
        if is_match(pot, word, min_len):
            print(word)


main("lesswords.txt", 3, "dcamteiut")
