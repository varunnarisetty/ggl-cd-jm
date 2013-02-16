'''
Created on Feb 15, 2013

alien numbers
converting between bases

@author: santosh
'''
import logging
import sys
import datetime

def main(filename):
    fd = open(filename, 'r')
    testCaseCount = int(fd.readline())
    opf = open(filename[:filename.find('.')] + '.out', 'w')
    for i in range(testCaseCount):
        (nmbr, src_digits, dest_digits) = fd.readline().split()
        deci_num = 0
        num_length = len(nmbr)
        base = len(src_digits)
        for indx, digit in enumerate(nmbr):
            deci_num += (src_digits.find(digit) * base ** (num_length - indx - 1))
        dest_num = ''
        base = len(dest_digits)
        while deci_num > 0:
            dest_num = str(dest_digits[deci_num % base]) + dest_num
            deci_num /= base
        opf.write('Case #' + str(i + 1) + ': ' + dest_num + '\n')
        
if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    if len(sys.argv) > 1:
        st = sys.argv[1]
    else : st = 'smpl.in'
    tm = datetime.datetime.now()
    main(st)
    print datetime.datetime.now() - tm
