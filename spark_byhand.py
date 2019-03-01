# Here, we tried to implement a python TF-IDF for Spark by hand

# First, we count the number of texts to obtain the number of documents, an important metric
# to compute the TF-IDF score.

number_of_docs = texts.count()

# Through a function, we split the words and return a lower case version for continuity

import re
def tokenize(s):
  return re.split("\\W+", s.lower())

# We then Tokenize the text by mapping the function above to the texts

tokenized_text = texts.map(lambda (title,text): (title, tokenize(text)))

# In each document, we count the Word Frequency of each word

term_frequency = tokenized_text.flatMapValues(lambda x: x).countByValue())

#[TO ADD] NEED TO DIVIDE BY TOTAL NUMBER OF WORDS PER DOC!

# We then count how many times each words occurs in ALL the documents

document_frequency = tokenized_text.flatMapValues(lambda x: x).distinct()\
                        .map(lambda (title,word): (word,title)).countByKey()

import numpy as np

# We then compute the TF-IDF score using a function:

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

# We output the result of our function which gives us the TF-IDF

tf_idf_output = tf_idf(number_of_docs, term_frequency, document_frequency)
