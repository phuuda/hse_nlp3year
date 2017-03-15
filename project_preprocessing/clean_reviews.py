import os, re

def clean_text(text):
    cleantext = re.sub('( - )|(-[\s\n])|(\n-)', ' — ', text)
    cleantext = re.sub('D@ABBE', '', cleantext) #кто-то оставил свой ник внутри рецензии
    cleantext = re.sub('\n\d{1,2} из \d{1,2}[\n$]', '\n', cleantext, flags=re.DOTALL)
    cleantext = re.sub('(т\.к\.)|(т\. к\.)', 'т##к##', cleantext)
    cleantext = re.sub('(P\.S\.)|(P\. S\.)', 'P##S##', cleantext)
    cleantext = re.sub('( [А-ЯЁA-Z])\. ', '\\1## ', cleantext)
    cleantext = re.sub('([\s\n]\d)\. ', '\\1## ', cleantext)
    cleantext = re.sub('[\.\\\(\)]', ' ', cleantext)
    cleantext = re.sub('[\"\*\»\«\[\]\t\,\?\!\;—…©]', '', cleantext)
    cleantext = re.sub('\:\s', ' ', cleantext)
    cleantext = re.sub('т##к##', 'т.к.', cleantext)
    cleantext = re.sub('P##S##', 'P.S.', cleantext)
    cleantext = re.sub('( [А-ЯЁA-Z])## ', '\\1. ', cleantext)
    cleantext = re.sub('([\s\n]\d{1,2})## ', '\\1. ', cleantext)
    cleantext = re.sub('\s{2}', ' ', cleantext)
    return cleantext


abr = []
path = 'reviews'
if os.path.exists(path):
    #new_path = path + '_clean/'
    #try:
        #os.makedirs(new_path)
    #except:
        #pass
    for root, dirs, files in os.walk(path):
        for i in files:
            fr = open(root + '/' + i, 'r', encoding = 'utf-8')
            text1 = fr.read()
            fr.close()
            #abr += re.findall('[А-ЯЁа-яё\w\.]+?\.', text1)
            text2 = clean_text(text1)
            print(text2)
            print('-----------------------------------------------------------------')
#abr_set = { word for word in abr }
#for word in abr_set:
    #print(word)