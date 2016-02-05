'''
Created on Mar 2, 2013

@author: user
'''

if __name__ == '__main__':
    N=int(input())
    for i in range(N):
        kingdom=input()
        vowels=['a','e','i','o','u']
        a='a '
        ruler='king'
        if kingdom[-1] in vowels:
            ruler='queen'
        elif kingdom[-1] == 'y':
            a=''
            ruler='nobody'
        
        print("Case #%d: %s is ruled by %s%s."%(i+1,kingdom,a,ruler ))