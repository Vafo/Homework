
from ast import arg
import string

def get_words(s:str) -> list[str]:
    _nonalpha_symb = set(string.printable[62:])
    
    words = [""]
    index = 0
    already_out = True

    for ch in s:
        if ch not in _nonalpha_symb:
            words[index] += ch
            already_out = False
        else:
            if not already_out:
                words.append("")
                index += 1
                already_out = True

    return words[:-1]

def most_common_words(filepath, number_of_words = 3):
    
    words_occurence = {}

    with open(filepath, "r") as file:
        for line in file:
            words_in_line = get_words(line)
            
            for word in words_in_line:
                if word in words_occurence:
                    words_occurence[word] += 1
                else:
                    words_occurence[word] = 1

    words_occurence = sorted(words_occurence.items(), key = lambda key: key[1], reverse=True)
    res = [ name[0] for name in words_occurence[:number_of_words] ]

    return res


print(most_common_words("../data/lorem_ipsum.txt"))
print(most_common_words("../data/lorem_ipsum.txt", 5))
print(most_common_words("../data/lorem_ipsum.txt", 8))
