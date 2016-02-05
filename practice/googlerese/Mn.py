'''
Created on Mar 22, 2013

@author: user
'''
from pprint import pprint

if __name__ == '__main__':
    grs = '''ejp mysljylc kd kxveddknmc re jsicpdrysi
 rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
 de kr kd eoya kw aej tysr re ujdr lkgc jv'''  # googlerese

    eng='''our language is impossible to understand
 there are twenty six factorial possibilities
 so it is okay if you want to just give up'''   # english
    
    gmap=dict()
    
    from test.test_iterlen import len
    for i in range(len(grs)):
        gmap[grs[i]]=eng[i]
    gmap['q']='z'
    gmap['z']='q'
    
    T=int(input())
    for i in range(T):
        st=input()
        st1=str()
        for j in st: st1+=gmap[j]
        print("Case #%d: %s"%(i+1,st1))    
    