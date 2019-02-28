import os
import random

word_list = random.sample(list(map(lambda x: x.strip(), open('words.txt', 'r'))), k=700) #700 words that we are going to
#sample from

n_words = 100000

if not os.path.exists('documents'):
    os.mkdir('documents')

for i in range(5):#number of dir
    if not os.path.exists('documents/' + str(i)):
        os.mkdir('documents/' + str(i)) #create new document
    for j in range(10):#number of files in each directory
        count = n_words
        with open('documents/' + str(i) + '/text_' + str(j) + '.txt', 'w') as file:
            while count > 0:
                words = ' '.join(random.sample(word_list, k=10)) #write 10 words in file
                file.write(words + '\n')
                count -= 10 #random choices would not work (sampling with replacement, had to do it that way in order to
                #sample from the same words
    n_words *= 2 #from one file to the other - double the size