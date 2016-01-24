import nltk #Must install nltk and download db

from nltk.stem.wordnet import WordNetLemmatizer
wnl = WordNetLemmatizer() #lemmatizer finds synonyms of words

print "Hello! Sally's my name, sass is my game!"
while True:
	line = raw_input()
	tokens = nltk.word_tokenize(line)
	tagged = nltk.pos_tag(tokens)