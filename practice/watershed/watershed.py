'''
Created on Feb 16, 2013

@author: santosh
'''
import sys
import datetime
import logging


def getSmallestNeighbour(arry, x,y):
    ''' returns index of smallest value surrounding the value at position
    in case of tie N(North),W,E,S order is used'''
    ar=[]
    if y>0:
        ar.append((arry[x][y-1],x,y-1,0))#North
    if x>0:
        ar.append((arry[x-1][y],x-1,y,1))#West  
    if x<len(arry[0])-1:
        ar.append((arry[x+1][y],x+1,y,2))#East
    if y<len(arry)-1:
        ar.append((arry[x][y+1],x,y+1,3))#South
    ar.sort(key=lambda d:d[0])
    logging.info(ar)
    # see if it is sink: current element is smaller than all its surrounding elements
    if ar[0][0]>arry[x][y]:
        return (arry[x][y],x,y,-1)
    if ar[0][0]!=ar[1][0]:
        return ar[0]
    else :
        # tie : we return as per the direction of the item
        if ar[0][3]<ar[1][3]: return ar[0]
        else : return ar[1]
    
    
def connectNode(connected_map,smallest_neighbour,current_node):
def main(filename):
    fd=open(filename,'r')      
    testCount=int(fd.readline())
    for i in range(testCount):
        (m,n)=[int(item) for item in fd.readline().split()]
        alt_map=[]
        for i in range(m):
            alt_map.append([int(k) for k in fd.readline().split()])
        logging.info(alt_map)
        connected_map=[]
        for i in range(m):
            for j in range(n):
                connectNode(getSmallestNeighbour(alt_map, i, j),(alt_map[i][j],i,j,-1))
                

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        st = sys.argv[1]
    else : st = 'smpl.in'
    tm = datetime.datetime.now()
    main(st)
    print datetime.datetime.now() - tm
