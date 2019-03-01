hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/tfidf/input/*.txt \
-output /user/hadoop/tfidf/output1 \
-file /home/hadoop/mapper1.py \
-mapper /home/hadoop/mapper1.py \
-file /home/hadoop/reducer1.py \
-reducer /home/hadoop/reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/tfidf/output1 \
-output /user/hadoop/tfidf/output2 \
-file /home/hadoop/mapper2.py \
-mapper /home/hadoop/mapper2.py \
-file /home/hadoop/reducer2.py \
-reducer /home/hadoop/reducer2.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/tfidf/output2 \
-output /user/hadoop/tfidf/output3 \
-file /home/hadoop/mapper3.py \
-mapper /home/hadoop/mapper3.py \
-file /home/hadoop/reducer3_B.py \
-reducer /home/hadoop/reducer3_B.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/tfidf/output3 \
-output /user/hadoop/tfidf/output4 \
-file /home/hadoop/mapper4_B.py \
-mapper /home/hadoop/mapper4_B.py
