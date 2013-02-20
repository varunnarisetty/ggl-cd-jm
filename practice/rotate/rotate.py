'''
Created on Feb 20, 2013

@author: santosh
'''
from pprint import pprint


def getConsecutiveCount(ar, element, x, y, inc_x, inc_y):
    '''
    returns sum of consecutive numbers
    '''
    n = len(ar)
    if 0 <= x < n and 0 <= y < n and ar[x][y] == element:
        return (getConsecutiveCount(ar, element, x - inc_x, y - inc_y, inc_x, inc_y) + 1 + getConsecutiveCount(ar, element, x + inc_x, y + inc_y, inc_x, inc_y))
        
    else: return 0
    

def main():
    fd = open('smpl.in')
    (n, n_cases) = [int(i) for i in fd.readline().strip().split()]
    
    ar = list()
    for i in range(n):
        k = []
        for j in range(n):
            k.append('.')
        ar.append(k) 
    for i in range(n):
        y = [i1 for i1 in fd.readline().strip() if i1 != '.']
        pprint(y)
        for j, el in enumerate(y):
            print('%d,%d - %s' % (n - j - 1, n - i - 1, el))
            ar[n - j - 1][n - i - 1] = el 
    pprint(ar)
    pprint(getConsecutiveCount(ar, ar[6][2], 6, 2, 0, 1))

if __name__ == '__main__':
    x = '..abc..'
    y = [i for i in x if i != '.']
    # pprint( y)
    main()
