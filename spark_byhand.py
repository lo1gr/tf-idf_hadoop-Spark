
number_of_docs = texts.count()

#split words
import re
def tokenize(s):
  return re.split("\\W+", s.lower())

#We Tokenize the text
tokenized_text = texts.map(lambda (title,text): (title, tokenize(text)))

#Count Word Frequency in each document
term_frequency = tokenized_text.flatMapValues(lambda x: x).countByValue())
#NEED TO DIVIDE BY TOTAL NUMBER OF WORDS PER DOC!


#how many times the words occur in ALL the documen
document_frequency = tokenized_text.flatMapValues(lambda x: x).distinct()\
                        .map(lambda (title,word): (word,title)).countByKey()

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
