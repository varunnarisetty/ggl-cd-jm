'''
Created on Feb 16, 2013

@author: santosh
'''
import sys
import datetime
import logging


def getSmallestNeighbour(arry, x, y):
    ''' returns index of smallest value surrounding the value at position
    in case of tie N(North),W,E,S order is used'''
    ar = []
    if y > 0:
        ar.append((arry[x][y - 1], x, y - 1, 0))  # North
    if x > 0:
        ar.append((arry[x - 1][y], x - 1, y, 1))  # West  
    if x < len(arry[0]) - 1:
        ar.append((arry[x + 1][y], x + 1, y, 2))  # East
    if y < len(arry) - 1:
        ar.append((arry[x][y + 1], x, y + 1, 3))  # South
    ar.sort(key=lambda d:d[0])
    logging.info('ar '+str(ar))
    # see if it is sink: current element is smaller than all its surrounding elements
    if ar[0][0] > arry[x][y]:
        return (arry[x][y], x, y, -1)
    if ar[0][0] != ar[1][0]:
        return ar[0]
    else :
        # tie : we return as per the direction of the item
        if ar[0][3] < ar[1][3]: return ar[0]
        else : return ar[1]
    
    
def connectNode(connected_map, smallest_neighbour, current_node):
    ''' connected_map is an array of sets
    makes smallest_neighbiur and current_node to belong to same set
    merges two sets if both nodes are already present
    creates new set if necessary
    '''
    
    logging.info('map '+str(connected_map))
    index_smallest_neighbour=(-1,-1)
    index_current_node=(-1,-1)
    for i,v in enumerate(connected_map):
        for j,v1 in enumerate(v):
            if v1[1]==current_node[1] and v1[2]==current_node[2]: index_current_node=(i,j)
            if v1[1]==smallest_neighbour[1] and v1[2]==smallest_neighbour[2]: index_smallest_neighbour=(i,j)
    # if nether of nodes exist create new set for the,
    if index_smallest_neighbour==(-1,-1) and index_current_node==(-1,-1):
        connected_map.append({smallest_neighbour,current_node})
    elif index_smallest_neighbour==(-1,-1) and index_current_node!=(-1,-1):
        connected_map[index_current_node[0]].add(smallest_neighbour)
    elif index_smallest_neighbour!=(-1,-1) and index_current_node==(-1,-1):
        connected_map[index_smallest_neighbour[0]].add(current_node)
    else:
        logging.info(index_smallest_neighbour)
        connected_map[index_current_node[0]]=connected_map[index_current_node[0]].update(connected_map[index_smallest_neighbour[0]])
        connected_map.pop(index_smallest_neighbour[0])
    return connected_map

def main(filename):
    fd = open(filename, 'r')      
    testCount = int(fd.readline())
    for i in range(testCount):
        (m, n) = [int(item) for item in fd.readline().split()]
        alt_map = []
        for i in range(m):
            alt_map.append([int(k) for k in fd.readline().split()])
        logging.info(alt_map)
        connected_map = []
        for i in range(m):
            for j in range(n):
                connected_map=connectNode(connected_map,getSmallestNeighbour(alt_map, i, j), (alt_map[i][j], i, j, -1))

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        st = sys.argv[1]
    else : st = 'smpl.in'
    tm = datetime.datetime.now()
    main(st)
    logging.info(datetime.datetime.now() - tm)
