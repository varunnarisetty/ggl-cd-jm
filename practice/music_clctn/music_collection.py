'''
Created on Mar 4, 2013

@author: santosh
'''


if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        print ('Case #%d:'%(t+1))
        N = int(input())
        songs = []
        for i in range(N): songs.append(input().lower()) 
        if N == 1: 
            print ('\"\"')
            continue
        for k, song in enumerate(songs):
            len_s = int(len(song))
            for n in range(1, len_s + 1):
                found=False
                # getting all substrings of length - sorted and set 
                n_len_subtrs = sorted(set([song[i:i + n]for i in range(0, len_s - n + 1)]))
                #print n_len_subtrs
                for each_substr in n_len_subtrs: 
                    matching_strs=[song1 for song1 in songs if song1!=song and each_substr in song1]
                    #print 'matching strs - %s'%(matching_strs)
                    found = len(matching_strs) == 0
                    if found:
                        print  ('\"%s\"'%(each_substr.upper()))
                        break
                if found: break
            if not found : print (":(")