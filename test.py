#!/usr/bin/python
from pyspark import SparkContext
sc = SparkContext("local", "first app")

text = sc.textFile("hdfs:///user/hadoop/tfidf/input/text_0.txt").cache().count()
print(text)


# from pyspark import SparkContext
# logFile = "file:///home/hadoop/spark-2.1.0-bin-hadoop2.7/README.md"
# sc = SparkContext("local", "first app")
# logData = sc.textFile(logFile).cache()
# numAs = logData.filter(lambda s: 'a' in s).count()
# numBs = logData.filter(lambda s: 'b' in s).count()
# print "Lines with a: %i, lines with b: %i" % (numAs, numBs)
