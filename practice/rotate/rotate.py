'''
Created on Feb 20, 2013

@author: santosh
'''
from pprint import pprint

def main():
    fd=open('smpl.in')
    (n,n_cases)=[int(i) for i in fd.readline().strip().split()]
    
    ar=list()
    for i in range(n):
        k=[]
        for j in range(n):
            k.append('.')
        ar.append(k) 
    pprint(ar)
    ar[1][1]='b'
    pprint(ar)
    for i in range(n):
        y=[i1 for i1 in fd.readline().strip() if i1!='.']
        pprint(y)
        for j,el in enumerate(y):
            print('%d,%d - %s'%(n-j-1,n-i-1,el))
            ar[n-j-1][n-i-1]=el 
            pprint(ar)
    pprint(ar)

if __name__ == '__main__':
    x='..abc..'
    y= [i for i in x if i!='.']
    #pprint( y)
    main()