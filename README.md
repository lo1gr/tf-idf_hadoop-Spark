# tf-idf_hadoop-Spark
Recreation of tf-idf in Hadoop and Spark using MapReduce in Python


Add this code every time to import the corresponding files we want (change the 0 to the corpus of documents we want to analyze)

for i in {0..9}; do
      wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/documents/0/text_$i.txt
done
