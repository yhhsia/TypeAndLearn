### This file contains static value that is referred in the game

import string
# player setting
initScore = 0
life = 5

width = 800
height = 800
attrList = ['slowdown', 'speedup', 'addlife', 'addscore']
pSpeedup = 60
pSlowdown = 80 
r = 40

# dict with alphabets
# https://stackoverflow.com/questions/19542820/creating-dict-where-keys-are-alphabet-letters-and-values-are-1-26-using-dict-com
alphabets = dict.fromkeys(string.ascii_lowercase, 0)
alphabets1 = dict.fromkeys(string.ascii_lowercase, 0)