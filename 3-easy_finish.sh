for i in {0..9}; do
      rm text_$i.txt
done

for i in {0..9}; do
      hdfs dfs -rm /user/hadoop/wc/input/text_$i.txt
done


for i in {1..3}; do
      hdfs dfs -rm -R /user/hadoop/wc/output$i
done
