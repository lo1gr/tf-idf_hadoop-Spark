# tf-idf_hadoop-Spark
Recreation of tf-idf in Hadoop and Spark using MapReduce in Python


to run 1-easy_setup.sh:
wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/1-easy_setup.sh
sh 1-easy_setup.sh

Add this code every time to import the corresponding files we want (change the 0 of documents/0/text to the corpus of documents we want to analyze):

for i in {0..9}; do
      wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/documents/0/text_$i.txt
      hdfs dfs -put text_$i.txt /user/hadoop/tfidf/input
done

wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/2-easy_run.sh
time sh 2-easy_run.sh

wget https://raw.githubusercontent.com/lo1gr/tf-idf_hadoop-Spark/master/3-easy_finish.sh
sh 1-easy_finish.sh


Ensuite pour le 2e mapreduce:




A FAIRE:
1- changer les documents tfidf car le tfidf est tjs a 0 (10 doc par file, 5 corpus en tout, double de taille entre chaque corpus, commence a 10k mots ou plus)
2- documenter tout sur le document word
3- noter les "real time" a chaque fois (5 nombres) + le faire pour plusieurs clusters:
jouer avec nombre d'instances et type d'instances sur AWS  + le faire 2 fois en utilisant
les 3mapper reducer et les 4mapper 3 reducer.
4- pySpark TFIDF finir: https://www.linkedin.com/pulse/understanding-tf-idf-first-principle-computation-apache-asimadi/ (a la main)
https://spark.apache.org/docs/2.2.0/ml-features.html (optimisé)
Mais modifications à faire car sur pySpark le TF est juste le nombre de fois le mot
apparait dans le doc, pas divise par le nombre de mots dans le doc. Donc a diviser.
Plus verifier que les ponctions sont bien enelevees a chaque fois. + possibilite
de le run pas ligne a ligne mais juste en faisant run un doc .py?
-> faire experimental analysis et noter les resultats pour differents types de clusters
5- Faire sur ggplot ou python les graphes qui montrent la difference de temps entre
instances, nombre d instances, taille de corpus, les 2 mapreduce et les 2 pySpark
6- Tout documenter sur le doc word au fur et a mesure
7- Le passer en Latex
8- pour faire des modifs au github, telechargez "github desktop", clonez le repo en local
et ensuite faites les modif comme ca en changeant les doc localemnt, commit puis push
(tout est montre sur l'application) - faire attention a bien le faire sur une branche
(ooption dans l'app), et la merge avec la branche principale si vous etes 100% surs. Sinon juste assurez vous de pousser vos commits assez souvent et s'assurer de pas se marcher sur les pieds car si on modifie en mm temps sur la branche principale ca bug.


Pour importer des files sur Spark:
wget the files as we were doing previously
type:
pySpark
then to import the files can do: texts = sc.wholeTextFiles("hdfs:///user/hadoop/tfidf/input").map(removePunctuation)   : check spark_optimized
