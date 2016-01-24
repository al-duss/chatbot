import re
import pickle
import string
#change this to whatever body of text you want to use
file_path = "shakespeare.txt"

def nonblank_lines(f):
    for l in f:
        line = l.rstrip()
        if line:
            yield line

file=open(file_path, 'r')
lines = file.read().split('\n')
print lines
text = ""
for line in lines:
	if not line.strip():
		l = line.split()
		print len(l)
		if not l[0].isupper():
			text = text + " " + line
words=text.lower().split()
for word in words:
	print word
	word = filter(str.isalnum, word)

firstWords = words
noOfWords = len(words) -1
word_pairs = []
for i in range(0,noOfWords):
	end = False
	word = words[i]
	if word[0] in ('[','(','"'):
		word = word[1:]
	if word[len(word)-1] in (';',')',']','"'):
		word = word[:-1]
	if word[len(word)-1] in ('.','?','!',':',','):
		word = word[:-1]
		word_pairs.append((word,"."))
	else:
		word = words[i+1]
		if word[0] in ('[','(','"'):
			word = word[1:]
		if word[len(word)-1] in (';',')',']','"','.','?','!',':',','):
			word = word[:-1]
		word_pairs.append((words[i], word))
		#print word
	#print word_pairs[i]
unique_pairs = {}
for pair in word_pairs:
	#print pair
	if pair in unique_pairs:
		unique_pairs[pair] = unique_pairs[pair] + 1
	else:
		unique_pairs[pair] = 1	
#for p in unique_pairs:
#	print p, unique_pairs[p]
pickle_file = open('shakepairs.pkl', 'wb')
wfie = open('shakewords.pkl', 'wb')
pickle.dump(unique_pairs, pickle_file)
pickle.dump(firstWords, wfie)
pickle_file.close()
file.close()
wfie.close()

print firstWords[1]