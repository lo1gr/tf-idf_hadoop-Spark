#!/usr/bin/python

# Using SparkContext, we create the connection to a spark cluster in order to allow
# spark functionalities (create RDDs, etc.)

from pyspark import SparkContext
sc = SparkContext("local", "first app")

# We define a function to remove punctuation and keep the words in lower case
# from the input texts

def removePunctuation(text):
    text=text.lower().strip()
    text=re.sub(“[^0-9a-zA-Z ]”, ”, text)
    return text

# We apply the function above to the input texts. Then, within the spark context, we gather
# the text inputs at the location where they are stored on the machine and transform them
# from a RDD to a Dataframe using .toDF (which causes errors when run...).

texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input").map(removePunctuation)
docs = texts.toDF()
docs = docs.toDF('label', 'sentence')
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

#END



#2:
# from pyspark.ml.feature import HashingTF, IDF, Tokenizer, CountVectorizer
#
# sentenceData = spark.createDataFrame([
#     (0.0, "Hi I heard about Spark"),
#     (0.0, "I wish Java could use case classes"),
#     (1.0, "Logistic regression models are neat")
# ], ["label", "sentence"])
#
# tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
# wordsData = tokenizer.transform(sentenceData)
#
#
# cv = CountVectorizer(inputCol="words", outputCol="rawFeatures")
# model = cv.fit(wordsData)
# featurizedData = model.transform(wordsData)
#
# idf = IDF(inputCol="rawFeatures", outputCol="features")
# idfModel = idf.fit(featurizedData)
# rescaledData = idfModel.transform(featurizedData)
#
# rescaledData.select("label", "features").show()
#
#
# from pyspark.sql.functions import split
# split_col = split(rescaledData['features'], ',')
# df = rescaledData.withColumn('NAME1', split_col.getItem(0))
# df = df.withColumn('NAME2', split_col.getItem(1))
# df.show()
#
#
# from pyspark.ml.linalg import Vectors, VectorUDT
# >>> test = udf(lambda vs: Vectors.dense(vs), VectorUDT())
#
#
# #try TF
# from pyspark.sql.functions import size
# >>> featurizedData.filter(size('words')>5).show()
#
# featurizedData = featurizedData.withColumn("size",size('words'))
#




# dont work:
# rescaledData.withColumn("test", rescaledData["features"].getItem(2))
# rescaledData.selectExpr("features[2]").show()
#from pyspark.sql.functions import lit, udf
#rescaledData.select("features", lit(2)).show()







# rescaledData.schema["features"].dataType
#
# rescaledData.withColumn('tf', rescaledData['features'] / rescaledData['size'])
#
#
#
# tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
# remover = StopWordsRemover(inputCol="words",
# outputCol="filtered")
#
# hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures")
# # cv = CountVectorizer(inputCol="filtered", outputCol="rawFeatures")
#
# idf = IDF(inputCol="rawFeatures", outputCol="features")
#
# pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf])
# # pipeline2 = Pipeline(stages=[tokenizer, remover, cv, idf])
#
# model = pipeline.fit(docs)
# # model2 = pipeline2.fit(docs)
#
# results = model.transform(docs)
#results2 = model2.transform(docs)

#From website: example of TFIDF

# from pyspark.ml.feature import HashingTF, IDF, Tokenizer
#
# sentenceData = spark.createDataFrame([
#     (0.0, "Hi I heard about Spark"),
#     (0.0, "I wish Java could use case classes"),
#     (1.0, "Logistic regression models are neat")
# ], ["label", "sentence"])
#
# tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
# wordsData = tokenizer.transform(sentenceData)
#
# hashingTF = HashingTF(inputCol="words", outputCol="rawFeatures", numFeatures=20)
# featurizedData2 = hashingTF.transform(wordsData)
#
# idf2 = IDF(inputCol="rawFeatures", outputCol="features")
# idfModel2 = idf2.fit(featurizedData2)
# rescaledData2 = idfModel2.transform(featurizedData2)
#
# rescaledData2.select("label", "features").show()
