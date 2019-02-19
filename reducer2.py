#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
prev_filename = None
current_count = 0
word = None
N=0
dic={}
temp_arr=[]

#input <filename, word#count>
for line in sys.stdin:
    line = line.strip()
    temp_arr.append(line)
    filename,wordcount = line.split('\t', 1)
    word,count = wordcount.split(' ', 1)


    # convert count to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    if prev_filename == filename:
        N+=count #number of words in document
    else:
      #means we are done with this file or havent started the first file yet
       if prev_filename: #if it is not None
            dic[prev_filename]=N
            N=0 #so that first count is counted

       prev_filename = filename
       N+=count #so that first count is counted
       
# do not forget to take into account the last one!
dic[prev_filename]=N

#temp_arr contains all the lines in stdin to be analyzed again.
for j in temp_arr:
    filename,wordcount = j.split('\t', 1)
    word,count = wordcount.split(' ', 1)
    for i in dic:
        if filename == i:
           wf=word+' '+filename
           nN=count+' '+str(dic[i]) #count of word in doc  and total count of words in same doc
           print '%s\t%s' % (wf,nN)

           #output <word#filename, n#N>
