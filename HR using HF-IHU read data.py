import os
import glob
import re

from collections import Counter

# Preparing Data to be used

dirs=os.listdir("fao")

dirs=sorted(dirs)
keyfiles = [f for f in dirs  if f.endswith('.key')]
txtfiles = [f for f in dirs if f.endswith('.txt')]

content=[]
allkeys=[]

for i in range(len(keyfiles)):
	allkeys.append(open("fao/"+keyfiles[i],"r").read())
	content.append(open("fao/"+txtfiles[i],"r").read())

#print content[6]	
#content=content.lower()

keywords=[]
for j in range(len(keyfiles)):
	keywords.append(allkeys[j].split('\n'))

cleantext=[]
regex=re.compile('[^a-zA-Z\ ]')
#regex = re.compile('[,\.!?/:()0-9;\n]')
for k in range(len(txtfiles)):
	cleantext.append(regex.sub('',content[k].lower()))
	#cleantext=re.sub('[^a-z\ ]+','',open('/home/anubhav/Desktop/naum/saurav-tagging/data/fao/'+txtfiles[k],"r").read())
	#print(cleantext)




#print cleantext[22]
allwords=[]
for n in range(len(txtfiles)):
	allwords.append(cleantext[n].split())

THFM = {}
HFM = {}

for i in range(1):
	for term in allwords[i]:
		if term not in THFM.keys():
			THFM[term]={}
		for keyword in keywords[i]:
			if keyword not in THFM[term].keys():
				THFM[term][keyword]=1
			else:
				THFM[term][keyword]+=1

			if keyword not in HFM.keys():
				HFM[keyword]={}
			if term not in HFM[keyword].keys():
				HFM[keyword][term]=1
			else:
				HFM[keyword][term]+=1


print THFM["national"]
print THFM["national"].keys()
print sum(THFM["national"].values())

print HFM["Forests"] 



'''
count=[]
for m in range(len(txtfiles)):
	count.append(Counter(allwords[m]))

print allwords[1][1]

wordfreq=[]

for m in range(len(txtfiles)):
	wordfreq.append(sorted(count[1].items(),key=lambda item: item[1],reverse=True))
#wordfreq=sorted(count[1].keys(), reverse=True)
#wordfreq2=list(reversed(wordfreq))
print wordfreq[55][4][0]
'''