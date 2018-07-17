# 3)	Заменить в произвольной строке согласные буквы на гласные.

import random
def consonant_line(line):
    VOVEL_LETTERS = ["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N",
                     "P", "Q", "R", "S", "T", "V", "W", "X", "Y", "Z"]
    CONSONANT_LETTERS = ["A", "E", "I", "O", "U", "Y"]
    consonant_list = []
    consonant_line = ' '

    for char in line:
        if char.upper() in CONSONANT_LETTERS:
            char = VOVEL_LETTERS[random.randint(0, len(VOVEL_LETTERS) - 1)].lower()
        consonant_list.append(char)
        consonant_line = ''.join(consonant_list)
    return consonant_line

line = 'The voice from the telescreen was still pouring forth its tale of prisoners and ' \
       'booty and slaughter, but the shouting outside had died down a little'
print(consonant_line(line))

