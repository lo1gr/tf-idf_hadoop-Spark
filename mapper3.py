#!/usr/bin/env python

import sys
import os

#input: <<word#documentName>, <n#N>>
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    wordfilename,nN=line.split('\t',1)
    word,filename=wordfilename.split(' ',1)
    out=filename+' '+nN+' '+str(1)
    print '%s\t%s' % (word,out)

    #output: <word,filename#nN#1>
