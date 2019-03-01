#!/usr/bin/python

# Using SparkContext, we create the connection to a spark cluster in order to allow
# spark functionalities (create RDDs, etc.)

from pyspark import SparkContext

sc = SparkContext()

# Within the spark context, we gather the text inputs at the location where they are
# stored on the machine and transform them from a RDD to a Dataframe using .toDF (which
# causes errors when run...)

texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input")
docs = texts.toDF('label', 'sentence')
docs.show(2)

# We start with a set of sentences and we split each sentence into words using
# a Tokenizer.

from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer, StopWordsRemover
from pyspark.ml import Pipeline

tokenizer = Tokenizer(inputCol="sentence", outputCol="words")

# We remove stopwords using StopWordsRemover

remover = StopWordsRemover(inputCol="words",
outputCol="filtered")

# We then vectorize the results for further processing

cv = CountVectorizer(inputCol="words", outputCol="rawFeatures")

# The vectorized rawFeatures are passed to the IDF, which rescales them.

idf = IDF(inputCol="rawFeatures", outputCol="features")

# We combine the previous steps into a spark pipeline

pipeline = Pipeline(stages=[tokenizer, remover, cv, idf])

# And fit the pipeline to the documents that we prepared in the first lines of code

model = pipeline.fit(docs)

# Lastly use the transform function to output our TFIDF results

results = model.transform(docs)
