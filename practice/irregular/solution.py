'''
Created on Mar 5, 2013

@author: user
'''
import sys
 
f = open(sys.argv[1])
T = int(f.readline())
for t in range(T):
    spell, vowels = f.readline().strip(), []
    for i, c in enumerate(spell):
        if c in "aeiou":    vowels += [i]               # Note the location of all vowels
 
    answer = "Nothing."
    for i in range(len(vowels) - 2):                    # For each vowel
        start = spell[vowels[i]:vowels[i + 1] + 1]      # Take minimum starting word from here (just to next vowel)
        if start in spell[vowels[i + 2] + 1:]:          # Skip one vowel for middle word, then see if 'start' is repeated
            answer = "Spell!"           
 
    print ("Case #%d: %s" % (t + 1, answer))