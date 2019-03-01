#!/usr/bin/python

from pyspark import SparkContext
sc = SparkContext("local", "first app")

def removePunctuation(text):
    text=text.lower().strip()
    text=re.sub(“[^0-9a-zA-Z ]”, ”, text)
    return text

texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input").map(removePunctuation)
docs = texts.toDF()
docs = docs.toDF('label', 'sentence')
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







rescaledData.schema["features"].dataType

rescaledData.withColumn('tf', rescaledData['features'] / rescaledData['size'])



tokenizer = Tokenizer(inputCol="sentence", outputCol="words")
remover = StopWordsRemover(inputCol="words",
outputCol="filtered")

hashingTF = HashingTF(inputCol="filtered", outputCol="rawFeatures")
# cv = CountVectorizer(inputCol="filtered", outputCol="rawFeatures")

idf = IDF(inputCol="rawFeatures", outputCol="features")

pipeline = Pipeline(stages=[tokenizer, remover, hashingTF, idf])
# pipeline2 = Pipeline(stages=[tokenizer, remover, cv, idf])

model = pipeline.fit(docs)
# model2 = pipeline2.fit(docs)

results = model.transform(docs)
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
