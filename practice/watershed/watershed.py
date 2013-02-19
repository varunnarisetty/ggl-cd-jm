'''
Created on Feb 16, 2013

@author: santosh
'''
import sys
import datetime
import logging
from platform import node
import itertools
import random

class Node:
    cnt=0
    def __init__(self, data, nextNode=None):
        self.__data = data
        self.__nextNode = nextNode
        self.__label=None

    def get_data(self):
        return self.__data


    def get_next_node(self):
        return self.__nextNode


    def set_data(self, value):
        self.__data = value


    def set_next_node(self, value):
        self.__nextNode = value

    def getLabel(self):
        '''recursively calculates and returns labels'''
        #logging.info(self)
        if self.__label==None:
            if self.__nextNode==None or self.__nextNode==self:
                self.__label=str(Node.cnt)
                Node.cnt+=1
            else:
                self.__label=self.__nextNode.getLabel()
        return self.__label
    
    def __str__(self):
        return str(self.__data)
    
    def __repr__(self):
        return str(self.getLabel())
    
def getSmallestNeighbour(arry, x, y):
    ''' returns index of smallest value surrounding the value at position
    in case of tie N(North),W,E,S order is used'''
    ar = [] 
    #logging.info('x,y '+str(x)+','+str(y))
    if y > 0:
        ar.append((arry[x][y - 1].get_data(), x, y - 1, 0))  # West
    if x > 0:
        ar.append((arry[x - 1][y].get_data(), x - 1, y, 1))  # North  
    if x < len(arry) - 1:
        ar.append((arry[x + 1][y].get_data(), x + 1, y, 2))  # South
    if y < len(arry[0]) - 1:
        ar.append((arry[x][y + 1].get_data(), x, y + 1, 3))  # East
    ar.sort(key=lambda d:d[0])
    #logging.info('ar '+str(ar))
    # see if it is sink: current element is smaller than all its surrounding elements
    if ar[0][0] >= arry[x][y].get_data():
        arry[x][y].set_next_node(arry[x][y])
        logging.info(str(arry[x][y])+'sync')
    elif ar[0][0] != ar[1][0]:
        arry[x][y].set_next_node(arry[ar[0][1]][ar[0][2]])
        logging.info('%d %d --> %d %d'%(x,y,ar[0][1],ar[0][2]))
    else :
        # tie : we return as per the direction of the item
        if ar[0][3] < ar[1][3]: 
            arry[x][y].set_next_node(arry[ar[0][1]][ar[0][2]])
            logging.info('%d %d --> %d %d'%(x,y,ar[0][1],ar[0][2]))    
        else : 
            arry[x][y].set_next_node(arry[ar[1][1]][ar[1][2]]) 
            logging.info('%d %d --> %d %d'%(x,y,ar[1][1],ar[1][2]))
            

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        st = sys.argv[1]
    else : st = 'smpl.in'
    tm = datetime.datetime.now()
    fd = open(st, 'r')      
    testCount = int(fd.readline())
    for i in range(testCount):
        (m, n) = [int(item) for item in fd.readline().split()]
        alt_map = []
        for i in range(m):
            alt_map.append([Node(int(k)) for k in fd.readline().split()])
        #logging.info(alt_map)
        [getSmallestNeighbour(alt_map, i, j) for j in range(n) for i in range(m)]
        [j.getLabel() for i in alt_map for j in i ]
        logging.info(alt_map)
        print ('\n'.join(alt_map))
    logging.info(datetime.datetime.now() - tm)
