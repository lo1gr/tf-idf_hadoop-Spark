for i in {1..3}; do
      wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/mapper$i.py
done

for i in {1..2}; do
      wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/reducer$i.py
done

wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/reducer3_A.py

chmod +x *.py
hdfs dfs -mkdir /user/hadoop/wc
hdfs dfs -mkdir /user/hadoop/wc/input
