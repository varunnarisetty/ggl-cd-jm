#!/usr/bin/env python3
from pprint import pprint

########################################################################
#   Solves Google CodeJam 2010 Round 1A's problem A
#   Copyright (C) 2011  Santiago Alessandri
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.
#
#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.
#
#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.
#	
#   You can contact me at san.lt.ss@gmail.com
#   Visit my wiki at http://wiki.san-ss.com.ar
#   Visit my blog at http://blog.san-ss.com.ar
########################################################################

def solve():
    n, K = map(int, raw_input().split(' '))
    board = [['.' for i in range(n)] for j in range(n)]
    for i in range(n-1, -1, -1):
        # Load column n-i-1
        line = raw_input()
        for j in range(n):
            board[j][i] = line[j]
        # Apply gravity in that column
        for j in range(n-1, -1, -1):
            while board[j][i] == '.':
                for k in range(j, 0, -1):
                    board[k][i] = board[k-1][i]
                board[0][i] = '#'
    
    
    blue = False
    red = False
        
    # Check for Vertical and horizontal
    for i in range(n):
        s = ''.join(board[i])
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
        s = ''.join(board[j][i] for j in range(n))
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
    
    # Check for Diagonal Right-Down and Left-Down
    for i in range(n):
        j = 0
        s = ''.join(board[i+d][j+d] for d in range(n-i))
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
        s = ''.join(board[j+d][i+d] for d in range(n-i))
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
        
        s = ''.join(board[j+d][i-d] for d in range(i+1))
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
        s = ''.join(board[i+d][n-d-1] for d in range(n-i))
        if 'B' * K in s:
            blue = True
        if 'R' * K in s:
            red = True
    pprint(board)    
    if blue and red:
        return 'Both'
    if blue:
        return 'Blue'
    if red:
        return 'Red'
    return 'Neither'


if __name__ == '__main__':
    t = int(input())
    for case in range(1, t+1):
        print("Case #{0}: {1}".format(case, solve()))
