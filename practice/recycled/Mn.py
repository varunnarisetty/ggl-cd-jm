'''
Created on Mar 25, 2013

@author: user
'''
import collections
import logging
import time

if __name__ == '__main__':
    start_time = time.time()
    T = int(input())
    for t in range(T):
        inp = input().strip().split()
        (A, B) = (int(inp[0]), int(inp[1]))
        count = 0
        dbg_ls=set()
        for i in range(A, B + 1):
            # checking for recycled pairs
            ''' to prevent counting twice lets enforce first element in recycled
            pair is less than second element''' 
            str_i = str(i)
            len_i = len(str_i)
            for j in range(1, len_i):
                i_pair = int (str_i[j:] + str_i[:j])
                if i_pair > i and A <= i_pair <= B : 
                    count += 1
                    #if A==1111: print ("(%d,%d)"%(i,i_pair))
                    dbg_ls.add((i,i_pair))
        #print ('len of list : %d, len of set : %d'%(len(dbg_ls),len(set(dbg_ls))))
        #print( [x for x, y in collections.Counter(dbg_ls).items() if y > 1])
        print ('Case #%d: %d' % (t + 1, len(dbg_ls))) 
    logging.error('%d seconds '%(time.time() - start_time))

                
    
