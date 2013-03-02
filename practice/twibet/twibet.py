'''
Created on Mar 2, 2013

@author: user
'''

if __name__ == '__main__':
    N= int(input())
    for i in range(N):
        n=int(input())
        mappings=[int(x) for x in input().strip().split()]
        counts=[]
        dq=[]
        cnt=0
        for index in range(1,n+1):
            cnt+=1;
            dq.append()
        
        print ("Case #%d:"%(i+1))
        print('\n'.join(counts))