#!/usr/bin/python

import sys
import os


for line in sys.stdin:
    # filepath = os.environ["map_input_file"] 
    # filename = os.path.split(filepath)[-1]
    filename = os.getenv('line')
    filename1 = os.environ('map_input_file')
    # filename2 = os.getenv("map_input_file")
    # print(file_name,' ',"filename2")
    # print(os.readlink('/proc/self/fd/0'))
    print(filename,' ',filename1)