#!/usr/bin/python
from pyspark import SparkConf, SparkContext
conf = (SparkConf()
         .setMaster("local")
         .setAppName("My app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

text = sc.textFile("hdfs:///user/hadoop/tfidf/input/text_0.txt")
text.count()
