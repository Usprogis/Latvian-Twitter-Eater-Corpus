import re 
import time

cot = 0
f = open("lv_positive_words_from_pumpurs.txt", "r")
text = []
for x in f:
	text.append(x.replace("\n",""))
f.close()
dictOfKeywords = { i : 0 for i in text }
print(dictOfKeywords)

wri = open("positive_tweets.txt", "w")
f = open("tweets.txt", "r")
for x in f:
	cot += 1
	print(cot)
	for key in dictOfKeywords:
		if x.find(key) != -1:
			dictOfKeywords[key] += 1
			wri.write(x)
			break

a = sorted(dictOfKeywords.items(), key=lambda x: x[1])    
print(a)

"""
time.sleep(30)

cot = 0
f = open("bad_emoji.txt", "r")
text = []
for x in f:
	text.append(x.replace("\n",""))
f.close()
dictOfKeywords = { i : 0 for i in text }

wri = open("bad_emoji_count.txt", "w")
f = open("tweets.txt", "r")
for x in f:
	cot += 1
	print(cot)
	for key in dictOfKeywords:
		if x.find(key) != -1:
			dictOfKeywords[key] += 1
			wri.write(x)

a = sorted(dictOfKeywords.items(), key=lambda x: x[1])    
print(a)
"""