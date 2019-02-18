hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/input/*.txt \
-output /user/hadoop/wc/poutput1 \
-file /home/hadoop/mapper1.py \
-mapper /home/hadoop/mapper1.py \
-file /home/hadoop/reducer1.py \
-reducer /home/hadoop/reducer1.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/poutput1 \
-output /user/hadoop/wc/poutput2 \
-file /home/hadoop/mapper2.py \
-mapper /home/hadoop/mapper2.py \
-file /home/hadoop/reducer2.py \
-reducer /home/hadoop/reducer2.py

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
-input /user/hadoop/wc/poutput2 \
-output /user/hadoop/wc/poutput3 \
-file /home/hadoop/mapper3.py \
-mapper /home/hadoop/mapper3.py \
-file /home/hadoop/reducer3_A.py \
-reducer /home/hadoop/reducer3_A.py