'''
Created on Mar 18, 2013

@author: user
'''
import sqlite3
import sys
from pprint import pprint

if __name__ == '__main__':
    con=sqlite3.connect('smpl.db')
    #con.execute('create table sm (id integer primary key autoincrement, nm text, desc text);')
    rows=[('s','d'),('d','l')]
    #con.executemany('insert into sm(nm,desc) values(?,?)',rows)
    #con.commit()
    for i in con.execute('select * from sm'):
        print  (i)
    
    #con.execute('create table smp2 (id integer primary key autoincrement, c text, d text)')    
    #con.executemany('insert into smp1(c,d) values(?,?)',rows)
    #con.commit()
    print('\n')
    #for i in con.execute('select c,d from smp1'):
      #  con.execute('insert into smp2(c,d) values(?,?)',i )
    
    
    for i in sys.stdin:
        prms=tuple(i.strip().split('|'));
        if len(prms) == 2:
            con.execute('insert into smp2(c,d) values(?,?)',prms) 
    con.commit()
    s=[i for i in con.execute('select * from smp2')]
    pprint (s)
    