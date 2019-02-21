for i in {0..9}; do
      rm text_$i.txt
done

for i in {0..9}; do
      hdfs dfs -rm /user/hadoop/tfidf/input/text_$i.txt
done


for i in {1..3}; do
      hdfs dfs -rm -R /user/hadoop/tfidf/output$i
done
