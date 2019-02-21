from operator import add

#wordcount in doc:
counts = text0.flatMap(lambda x: x.split(' ')) \
		.map(lambda x: (x, 1)) \
		.reduceByKey(add)

#total number words in document:
N0 = text0.flatMap(lambda x: x.split(' ')) \
		.count()
