#!/usr/bin/python

from pyspark import SparkContext, SparkSession
sc = SparkContext()

texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input")
docs = texts.toDF('label', 'sentence')
docs.show(2)

# In the following code segment, we start with a set of sentences. We split each
# sentence into words using Tokenizer. For each sentence (bag of words), we use
# HashingTF to hash the sentence into a feature vector. We use IDF to rescale the
#  feature vectors; this generally improves performance when using text
#  as features. Our feature vectors could then be passed to a learning algorithm.

from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer, StopWordsRemover
from pyspark.ml import Pipeline

tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
remover = StopWordsRemover(inputCol="words",
outputCol="filtered")

cv = CountVectorizer(inputCol="words", outputCol="rawFeatures")

idf = IDF(inputCol="rawFeatures", outputCol="features")

pipeline = Pipeline(stages=[tokenizer, remover, cv, idf])

model = pipeline.fit(docs)

results = model.transform(docs)
