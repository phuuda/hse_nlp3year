import os, re

fr = open('reviews.txt', encoding = 'utf-8')
text = fr.read()
fr.close()
reviews = re.findall('.+?\d\d\:\d\d\n', text, flags=re.DOTALL)
l = 0
for i in range(len(reviews)):
    review = re.sub('^.+?\n\n', '', reviews[i], flags=re.DOTALL)
    review = re.sub('\nпрямая ссылка.+?$', '', review, flags=re.DOTALL)
    review = re.sub('\n{2,}', '\n', review, flags=re.DOTALL)
    review = review.strip()
    print(review)
    print('-----------------------------------------------------------------')
    l += len(review.split())
    fw = open('reviews/' + str(i+1) + '.txt', 'w', encoding = 'utf-8')
    fw.write(review)
    fw.close()
print(i)
print(l)