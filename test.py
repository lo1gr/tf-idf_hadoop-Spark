#!/usr/bin/python

text = sc.textFile("hdfs:///user/hadoop/tfidf/input/text_0.txt")
text.count()
