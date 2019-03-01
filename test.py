# texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input")
text = sc.textFile("hdfs:///user/hadoop/tfidf/input/text_0.txt")
text.count()
