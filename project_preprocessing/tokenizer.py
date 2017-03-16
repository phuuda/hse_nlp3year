import re
import os
import csv

token_file = open('tokens.csv', 'w', encoding = 'utf-8')
abbrev_file = open('abbreviations.txt', 'r', encoding = 'utf-8')

s1 = abbrev_file.read()
abbreviations = s1.split() # keep with .

time_stamp = '[0-9]{1,2}:[0-9]{1,2}'

punctuation = ['\.', ',', '\"', '?!', '???', '?', '!!!', '!', '[а-яА-Я](:)',
               '…', '—', '©']

doc_id = 1
for root, dirs, files in os.walk('./reviews_clean'):
    for file in files:
        if file.endswith('.txt'):
            f = open(root + '/' + file, 'r', encoding = 'utf-8')
            s2 = f.read()

                            # ',' -> ' ,'
            
            text = s2.split() # list of words + glued puncutation
                             # separates names like 'James M. Cain'

            token_id = 1

            punc_count = 0
            for x in text:
                for i in range(9):
                    if x.endswith(punctuation[i]):
                        
                        additional_token_id = token_id + 1
                        additional_token = punctuation[i]

                        token = x.replace(punctuation[i], '')

                        fields = [doc_id, token_id, token]
                        additional_fields = [doc_id, additional_token_id,
                                             additional_token]

                        writer = csv.writer(token_file)
                        writer.writerow(fields)
                        writer.writerow(additional_fields)

                        token_id += 2
                        punc_count += 1

                if punc_count == 0:
                    # check other conditions ?

                    token = x
                    fields = [doc_id, token_id, token]

                    writer = csv.writer(token_file)
                    writer.writerow(fields)

                    token_id += 1
                    


            # token
            #

            doc_id += 1
            f.close()

            
