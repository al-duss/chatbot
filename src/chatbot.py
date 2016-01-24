import re
import pickle
import string
import random
def findNext (curr, pairdict, worddict):
    if curr in worddict:
        #print curr + "\n"
        wBest = curr
        pBest = 0
        candidates = []
        for pair in pairdict.keys():
            if pair[0] == curr:
                for i in range(pairdict[pair]):
                    candidates.append(pair[1])
                # if pairdict[pair]>pBest:
                #     wBest = pair[1]
                #     pBest = pairdict[pair]
        return candidates[random.randint(0, len(candidates) -1)]
    else:
        print "not found"


pairfile= "pairs.pkl"
wordfile = "words.pkl"
wfile = open(wordfile, 'rb')
pfile = open(pairfile, 'rb')
tuple_data = pickle.load(pfile)
word_data = pickle.load(wfile)
print word_data
print "Hi I'm Sally."
while True:
    sentence = raw_input().lower().split()
    seed = sentence[random.randint(0,len(sentence)-1)]
#print type (word_data)
#if seed in word_data:
   # print 'yes'
#else:
    #print 'not in list'
    phrase = ""
    while seed[len(seed)-1] != '.':
        phrase += " " + seed
        seed = findNext(seed, tuple_data, word_data)

    print phrase + "."
