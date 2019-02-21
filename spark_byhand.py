from operator import add
import math

#number docs
D = 10

#wordcount in doc:
counts0 = text0.flatMap(lambda x: x.split(' ')) \
		.map(lambda x: (x, 1)) \
		.reduceByKey(add)

#total number words in document:
N0 = text0.flatMap(lambda x: x.split(' ')) \
		.count()

tf0 = counts0.map(lambda x: x/N0)

#number of documents with term t in it   term t0, t1...  #docs is Value
#want output:
# <t0,NumDocs>
# <t1,NumDocs>
# <t2,NumDocs>
#if doc
counts0

idf0 = log(D/)

TF(t) = (Number of times term t appears in a document) / (Total number of terms in the document)
IDF(t) = log_e(Total number of documents / Number of documents with term t in it).

tfidf= TF*IDF

#goes over ALL LINES looking for 1 WORD
#need to go over ALL DOCS looking for ALL WORDS appearing
input.filter(lambda line : "error" in line).count()

#1- get all existing keys in all the docs
#filter acoording to those keys to find if doc contains.




# from pyspark.ml.feature import HashingTF, IDF, Tokenizer
# from pyspark.ml.feature import StringIndexer
# from pyspark.ml import Pipeline
#
# tokenizer = Tokenizer(inputCol="text", outputCol="words")
# hashtf = HashingTF(numFeatures=2**16, inputCol="words", outputCol='tf')
# idf = IDF(inputCol='tf', outputCol="features", minDocFreq=5) #minDocFreq: remove sparse terms
# label_stringIdx = StringIndexer(inputCol = "target", outputCol = "label")
# pipeline = Pipeline(stages=[tokenizer, hashtf, idf, label_stringIdx])
#
# pipelineFit = pipeline.fit(train_set)
# train_df = pipelineFit.transform(train_set)
# val_df = pipelineFit.transform(val_set)
# train_df.show(5)
