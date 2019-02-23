 # sc.textFile(“/path/to/dir”), where it returns an rdd of string or
 # use sc.wholeTextFiles(“/path/to/dir”) to get an RDD of (key,value) pairs
 # where key is the path and value is the content from each file.


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

# Comprendre:
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
# featurizedData = hashingTF.transform(wordsData)
# # alternatively, CountVectorizer can also be used to get term frequency vectors
#
# idf = IDF(inputCol="rawFeatures", outputCol="features")
# idfModel = idf.fit(featurizedData)
# rescaledData = idfModel.transform(featurizedData)
#
# rescaledData.select("label", "features").show()



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



# cv = CountVectorizer(inputCol="filtered", outputCol="rawFeatures")
# pipeline2 = Pipeline(stages=[tokenizer, remover, cv, idf])
# model2 = pipeline2.fit(docs)
#results = model.transform(docs)
#results2 = model2.transform(docs)


number_of_docs = texts.count()

#split words
import re
def tokenize(s):
  return re.split("\\W+", s.lower())

#We Tokenize the text
tokenized_text = texts.map(lambda (title,text): (title, tokenize(text)))

#Count Word Frequency in each document
term_frequency = tokenized_text.flatMapValues(lambda x: x).countByValue()\
                    .map(lambda x: x[1]=x[1]/)
#NEED TO DIVIDE BY TOTAL NUMBER OF WORDS PER DOC!


#how many times the words occur in ALL the documen
document_frequency = tokenized_text.flatMapValues(lambda x: x).distinct()\
                        .map(lambda (title,word): (word,title)).countByKey()
#

document_frequency.items()[:10]

import numpy as np

#compute tf_idf
# term_frequency: ((text0,text1..., word), count)
#doc freq: <word,count>
def tf_idf(number_of_docs, term_frequency, document_frequency):
    result = []
    for key, value in term_frequency.items():
        doc = key[0]
        term = key[1]
        df = document_frequency[term]
        if (df>0):
          tf_idf = float(value)*np.log(number_of_docs/df)

        result.append({"doc":doc, "score":tf_idf, "term":term})
    return result



tf_idf_output = tf_idf(number_of_docs, term_frequency, document_frequency)

tf_idf_output[:10]
