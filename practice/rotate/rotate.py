'''
Created on Feb 20, 2013

@author: santosh
'''
from pprint import pprint
import re
import sys


def getConsecutiveCount(ar, element, x, y, inc_x, inc_y):
    '''
    returns sum of consecutive numbers
    '''
    n = len(ar)
    if 0 <= x < n and 0 <= y < n and ar[x][y] == element:
        return (1 + getConsecutiveCount(ar, element, x + inc_x, y + inc_y, inc_x, inc_y))
    else: 
        return 0
    

def main():
    if len(sys.argv) > 1:
        st = sys.argv[1]
    else : st = 'smpl.in'
    
    fd = open(st)
    opf = open(st[:st.find('.')] + '.out', 'w')
    N = int(fd.readline())
    for testCase in range(N): 
        (n, n_seq) = [int(i) for i in fd.readline().strip().split()]
        
        ar = list()
        for i in range(n):
            k = []
            for j in range(n):
                k.append('.')
            ar.append(k) 
        for i in range(n):
            y = reversed([i1 for i1 in fd.readline().strip() if i1 != '.'])
            # pprint(y)
            for j, el in enumerate(y):
                # print('%d,%d - %s' % (n - j - 1, n - i - 1, el))
                ar[n - j - 1][n - i - 1] = el 
        # pprint(ar)
        
        (isR, isB) = (None, None)
        
        # scan rows for consecutive nums
        # print 'scanning rows'
        for i in ar:
            ii = ''.join(i)
            if isB == None and ('B' * n_seq) in ii: isB = True
            if isR == None and ('R' * n_seq) in ii: isR = True
        
        # scan cols for consecutive nums
        if isB == None or isR == None:
            # print 'scanning cols',isR,isB
            for i in range(n):
                ii = ''.join([ar[j][i] for j in range(n)])
                # print ii
                if isB == None and ('B' * n_seq) in ii: isB = True
                if isR == None and ('R' * n_seq) in ii: isR = True
                # print isB,isR
        # now look for diagonals
        if isB == None or isR == None:
            # print 'scanning diagonals',isR,isB
            for i in range(n):
                for j in range(n):
                    if ar[i][j] != '.':
                        if isR == None and ar[i][j] == 'R':
                            leftCnt = getConsecutiveCount(ar, 'R', i - 1, j - 1, -1, -1)
                            rightCnt = getConsecutiveCount(ar, 'R', i + 1, j + 1, 1, 1)
                            # print 'calculating ',leftCnt,',',rightCnt
                            cnt = leftCnt + 1 + rightCnt
                            # print 'diag R',i,j,cnt,n_seq
                            if cnt >= n_seq : isR = cnt
                            
                        if isB == None and ar[i][j] == 'B':
                            # print 'calculating ',getConsecutiveCount(ar, 'B', i, j, -1, -1),',',getConsecutiveCount(ar, 'B', i, j, 1, 1)
                            cnt = getConsecutiveCount(ar, 'B', i - 1, j - 1, -1, -1) + 1 + getConsecutiveCount(ar, 'B', i + 1, j + 1, 1, 1)
                            # print 'diag B',i,j,cnt,n_seq
                            if cnt >= n_seq : isB = cnt
                        
        ops = ''    
        if isB != None and isR != None: ops = 'Both'
        elif isB == None and isR == None : ops = 'Neither'
        elif isB != None : ops = 'Blue'
        else : ops = 'Red'
        opf.write('Case #%d: %s\n'%(testCase+1,ops))
        

if __name__ == '__main__':
    x = '..abc..'
    y = [i for i in x if i != '.']
    # pprint( y)
    main()
