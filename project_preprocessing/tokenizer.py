import re
import os
import csv

token_file2 = open('tokens.txt', 'w', encoding = 'utf-8')

abbrev_file = open('abbreviations.txt', 'r', encoding = 'utf-8')

s1 = abbrev_file.read()


abbreviations = s1.split() # keep with .

time_stamp = '[0-9]{1,2}:[0-9]{1,2}'

punctuation = ['\.', '\,', '\"', '\?\!', '\?\?\?', '\?', '\!\!\!', '\!', '\:', '\;', '\(', '\)',
               '…', '—', '©', '\/']

doc_id = 1
for root, dirs, files in os.walk('./reviews_clean'):
    for file in files:
        if file.endswith('.txt'):
            f = open(root + '/' + file, 'r', encoding = 'utf-8')
            s2 = f.read()

            for i in range(len(punctuation)):
                search = punctuation[i]
                punct_in_s2 = re.findall(search, s2)
                
                if punct_in_s2:
                    for m in punct_in_s2:
                        s2 = s2.replace(m, ' ' + m + ' ')

                            # ',' -> ' ,'
            
            text = s2.split() # list of words + glued puncutation
                             # separates names like 'James M. Cain'

            token_id = 1
            for x in text:
                fields = str(doc_id) + '\t' + str(token_id) + '\t' + x + '\n'
                token_file2.write(fields)

                token_id += 1
                
##                punc_count = 0
##                for i in range(9):


                    
##                    if x.endswith(punctuation[i]):
##                        
##                        additional_token_id = token_id + 1
##                        additional_token = punctuation[i]
##                        
##                        #print(additional_token)
##                        
##                        token = x.replace(punctuation[i], '')
##                        #print(token)
##
##                        fields = str(doc_id) + '\t' + str(token_id) + '\t' + token + '\n'
##                        additional_fields = str(doc_id) + '\t' + str(additional_token_id) + '\t' + additional_token + '\n'
##
##
##                        token_file2.write(str(doc_id) + '\t' + str(token_id) + '\t' + token + '\n')
##                        token_file2.write(str(doc_id) + '\t' + str(additional_token_id) + '\t' + additional_token + '\n')
##
##                        token_id += 2
##                        punc_count += 1
##
##                if punc_count == 0:
##                    # check other conditions ?
##
##                    token = x
##                    fields = str(doc_id) + '\t' + str(token_id) + '\t' + token + '\n'
##
##
##                    token_file2.write(str(doc_id) + '\t' + str(token_id) + '\t' + token + '\n')
##
##                    token_id += 1
                    



            doc_id += 1
            f.close()

            
