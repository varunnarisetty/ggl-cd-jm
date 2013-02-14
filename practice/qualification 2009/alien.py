#!/usr/bin/python
# Alien Language
import sys
import logging
import collections
import re

logging.basicConfig(level=logging.INFO)

def main(filename):
    fd = open(filename)
    op = open(filename[:-2]+'out', mode='w')
    (L, D, N) = [int(i) for i in fd.readline().strip().split()]
    logging.info('L=' + str(L) + ' D=' + str(D) + ' N=' + str(N))
    words = set()
    for i in range(D):
        words.add( fd.readline().strip())
    tests = []
    for i in range(N):
        tests.append(fd.readline().strip().replace('(','[').replace(')', ']'))
        
    logging.info (str(words) + '\n' + str(tests))
    cnt=[0]*N
    for wrd in words:
        for i, test in enumerate(tests):
            logging.debug(test)
            if re.search(test, wrd, 0):
                cnt[i]+=1
    
    for i, num in enumerate(cnt): 
        opf='Case #' + str(i+1) + ': ' + str(num)+'\n'
        op.write(opf)
    
    op.close()

if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
