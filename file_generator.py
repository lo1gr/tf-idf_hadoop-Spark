import os
import random

# We create a word list that randomly samples from 700 words

word_list = random.sample(list(map(lambda x: x.strip(), open('words.txt', 'r'))), k=700)

n_words = 100000

# We create a directory called 'documents' to hold our created file

if not os.path.exists('documents'):
    os.mkdir('documents')

# We then create further directories that will hold the scaled up versions of the documents that
# we want to test.

for i in range(5): # We want 5 directories
    if not os.path.exists('documents/' + str(i)):
        os.mkdir('documents/' + str(i)) # We create new directories called 'document' + their index
    for j in range(10):# Ranging from the number of files in each directory
        count = n_words
        with open('documents/' + str(i) + '/text_' + str(j) + '.txt', 'w') as file:
            while count > 0:
                words = ' '.join(random.sample(word_list, k=10)) # We write 10 words in file
                file.write(words + '\n')
                count -= 10 # As random choices would not work (sampling with replacement), we had to code it in that way in order to sample from the same words
    n_words *= 2 # Then, from one file to the other we double the size to obtain scaled versions
