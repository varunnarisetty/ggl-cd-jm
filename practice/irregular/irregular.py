'''
Created on Mar 5, 2013

@author: santosh

'''
import sys
import logging
import pprint

if __name__ == '__main__':
    logging.basicConfig(filename='dbg.log',level='DEBUG')
    logging.info("=======================================")
    F = open(sys.argv[1])
    T = int(F.readline())
    vowels = ['a', 'e', 'i', 'o', 'u']
    for t in range(T):
        spell = F.readline().strip()
        # get vowel indices
        vowel_indices = [i for i in range(len(spell)) if spell[i] in vowels]
        # atleast 5 vowels are needed to form a spell
        if len(vowel_indices) < 5: 
            print ('Case #%d: Nothing.' % (t + 1))
            continue
        logging.info(pprint.pformat(vowel_indices)+spell)
        found=False
        for i in range(0,len(vowel_indices)-3):
            word=spell[vowel_indices[i]:vowel_indices[i+1]+1]
            logging.info("%d: %s == %s"%(t+1,word,spell[vowel_indices[i+2]+1:]))
            if  word in  spell[vowel_indices[i+2]+1:]:
                found=True
                logging.debug('gotcha')
                break
        if found: print ("Case #%d: Spell!"%(t+1))
        else : print ('Case #%d: Nothing.' % (t + 1))
