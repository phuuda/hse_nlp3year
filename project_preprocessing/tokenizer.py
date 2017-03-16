import re
import os

token_file = open('tokens.csv', 'w', encoding = 'utf-8')

doc_id = 1
abbreviation = []
punctuation = ['\.', ',', '\"', '?!', '???', '?', '!!!', '!',
               '[0-9]{1,2}:[0-9]{1,2}',':', '—', '…', '©']

for root, dirs, files in os.walk('./reviews'):
    for file in files:
        if file.endswith('.txt'):
            f = open(root + '/' + file, 'r', encoding = 'utf-8')
            s = f.read()
            text = s.split() # list of words + glued puncutation

            token_id = 1
            
            for x in text:
                print(x)


            # token
            #


            # add token line to token_file

            
