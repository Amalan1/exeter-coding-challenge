from os import replace
import re
import csv
mydict={}
with open('french_dictionary.csv', mode='r') as infile:
    reader = csv.reader(infile)
    mydict = {rows[0]:rows[1] for rows in reader}
f1 = open('t8.shakespeare.txt',"r")
f2 = open('find_words.txt','r')
content = f1.read()
uniq1 = re.split("\s|(?<!\d)[,.](?!\d)",content)
uniq2 =set(wordss for lines in f2 for wordss in lines.strip('\n\t').split(" "))
for words in uniq1:
	for wordds in uniq2:
		if words == wordds:
			if wordds in mydict:
				content=content.replace(wordds,str(mydict[wordds]))
print(content)

