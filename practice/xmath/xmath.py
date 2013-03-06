'''
Created on Mar 6, 2013

@author: santosh
'''
import math
if __name__ == '__main__':
    N=2
    multiplicand=[N]
    P=10000-1
    
    for i in range(P):
        carry=[0]*len(multiplicand)
        result=[]
        #multiply
        j=len(multiplicand)-1
        while j>0:
            product=multiplicand[j]*N+carry[j]
            result.insert(0,product%10)
            carry[j-1]=product//10
            j-=1
        product=multiplicand[0]*N+carry[0]
        while product>0:
            result.insert(0,product%10)
            product=product//10
        multiplicand.clear()
        multiplicand.extend(result)
       
    [print (i,end='') for i in multiplicand]
    
    print ("\n%d"%(math.pow(N, P+1)))
