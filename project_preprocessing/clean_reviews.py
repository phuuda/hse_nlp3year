import os, re

def normalize_text(text):
    normtext = re.sub('( - )|(-[ \n])|([ \n]-)|(\n-)', ' — ', text) #нормализация тире
    normtext = re.sub(' — х ', '-х ', normtext)
    normtext = re.sub('([Тт]\.) ((к\.)|(д\.)|(ч\.)|(п\.)|(е\.)|(з\.))', '\\1\\2', normtext) #частые сокращения
    normtext = re.sub('([Pp]\. ?[Ss]\.?:?)|(ps )|(PS )', 'P.S. ', normtext)
    normtext = re.sub('[«»“„]', '"', normtext) #нормализация кавычек
    normtext = re.sub('\.{2,}', '… ', normtext) #нормализация многоточих
    normtext = re.sub('!{2,}', '!!!', normtext) #нормализация повторяющихся воскл./вопр. знаков
    normtext = re.sub('\?{2,}', '???', normtext) 
    normtext = re.sub('(!+\?+)|(\?+!+)', '?!', normtext)
    normtext = re.sub('\(с\)', '©', normtext) #нормализация знака ©
    normtext = re.sub('\t', ' ', normtext)
    normtext = re.sub(' {2,}', ' ', normtext) #нормализация пробелов
    normtext = re.sub(' \n', '\n', normtext)
    return normtext

def clean_text(text):
    cleantext = re.sub('— D@ABBE', '', text) #кто-то оставил свой ник внутри рецензии
    cleantext = re.sub('Typewrited by Hannabar in 13\/03\/2017\.', '', text) #странная строчка осталась
    #cleantext = re.sub('\n[\d\,]{1,2} из \d{1,2}[\n$]', '\n', cleantext, flags=re.DOTALL) #10 из 10
    #cleantext = re.sub('"', '', cleantext) #удаление кавычек?
    return cleantext

path = 'reviews'
texts = ''
if os.path.exists(path):
    new_path = path + '_clean/'
    try:
        os.makedirs(new_path)
    except:
        pass
    for root, dirs, files in os.walk(path):
        for i in files:
            fr = open(root + '/' + i, 'r', encoding = 'utf-8')
            text1 = fr.read()
            fr.close()
            text2 = normalize_text(text1)
            text2 = clean_text(text2)
            print(i)
            print(text2)
            texts += text2 + '\n'
            print('-----------------------------------------------------------------')
            #fw = open('reviews_clean/' + i, 'w', encoding = 'utf-8')
            #fw.write(text2)
            #fw.close() 

fw = open('texts.txt', 'w', encoding = 'utf-8')
fw.write(texts)
fw.close() 
   