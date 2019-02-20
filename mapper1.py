#!/usr/bin/python

import sys
import re
import os
# import nltk
# from nltk.corpus import stopwords
#
# stop_words = set(stopwords.words('english'))

stopwords= ['a','able','about','across','after','all','almost','also','am','among','an','and','any','are','as','at','be','because','been','but','by',
            'can','cannot','could','dear','did','do','does','either','else','ever','every','for','from','get','got','had','has','have','he','her','hers',
            'him','his','how','however','i','if','in','into','is','it','its','just','least','let','like','likely','may','me','might','most','must','my',
            'neither','no','nor','not','of','off','often','on','only','or','other','our','own','rather','said','say','says','she','should','since','so',
            'some','than','that','the','their','them','then','there','these','they','this','tis','to','too','twas','us','wants','was','we','were','what',
            'when','where','which','while','who','whom','why','will','with','would','yet','you','your'];


# input comes from STDIN (standard input)
for line in sys.stdin:
    try:
        input_file = os.environ['mapreduce_map_input_file']
    except KeyError:
        input_file = os.environ['map_input_file']
    #filename = os.environ["map_input_file"]
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    words = line.split()

    # increase counters
    for word in words:
        word=word.lower();
        #remove everything that isn't a character or number
        word=re.sub(r'[\W_]+', '', word)
        if word not in stopwords:
            out=word+' '+input_file;
            print '%s\t%s' % (out, 1)
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1
        #output: <word+' '+filename,1>
