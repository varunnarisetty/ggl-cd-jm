'''
Created on Mar 22, 2013

@author: user
'''
from pprint import pprint

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        totals = input().strip().split()
        totals = [int(i) for i in totals]
        (N, S, P) = (totals.pop(0), totals.pop(0), totals.pop(0))
        (nl, sl) = (list(), list())  # normal, special
        ''' To nl, we add Tr if True i's best scorce equals P, False otherwise
        To sl, we add True only if its best score matches P and corresponding nl has False;
        we don't want to count twice'''
        
        for ti in totals:
            (d, r) = (ti // 3, ti % 3)
            if(ti < 2):
                best_score_nl = r
                best_score_sl = -1
            elif(ti > 28):
                best_score_nl = 10
                best_score_sl = -1
            else:
                if r == 0:
                    best_score_nl = d
                    best_score_sl = d + 1
                elif r == 1:
                    best_score_nl = d + 1
                    best_score_sl = d + 1
                else:
                    best_score_nl = d + 1
                    best_score_sl = d + 2
            nl.append(best_score_nl >= P)
            sl.append(nl[-1] == False and best_score_sl >= P)
        sm = sum([1 for l in sl if l])
        if S < sm : sm = S
        print ('Case #%d: %d' % (i + 1, sum([1 for l in nl if l]) + sm))
            
