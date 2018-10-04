from gensim import corpora
import tempfile, os, sys, glob
from gensim import corpora, models, similarities

from summarize_codes import *
from template import *

def test_file(filename):
	TEMP_FOLDER = "./model/"

	test_script = filename

	documents = []
	documents.append(uccfilereader(test_script))

	stoplist = set('for a of the and to in'.split())
	texts = [[word for word in document.lower().split() if word not in stoplist]
         	for document in documents]

	dictionary = corpora.Dictionary.load_from_text(TEMP_FOLDER+"dictionary.txt")
	corpus = [dictionary.doc2bow(text) for text in texts]

	tfidf = models.TfidfModel.load(TEMP_FOLDER+"model.tfidf")
	corpus_tfidf = tfidf[corpus]


	lsi = models.LsiModel.load(TEMP_FOLDER+"model.lsi")
	corpus_lsi = lsi[corpus_tfidf]

	topic_dict = {}
	for i in range(0,100):
		topic_dict[i] = dict(lsi.show_topic(i, topn=40)).keys()

	doc_dict = dict(corpus_lsi[0])
#    doc_keys_sorted = sorted(doc_dict, key=lambda d: abs(doc_dict[d]))[-8:]
	
	return doc_dict, topic_dict


print("#############-------------------------------############")
print("### ask me about symptoms, problems of this conversation")
print("#############-------------------------------############")

print("---------------------------------------------------------")


while True:

	inp = input("Please provide path of file to analyze: ")
	print("give me a sec...")
	print("ask me about symptoms, problems of this conversation")

	doc_dict, topic_dict = test_file(inp)

	while True:
		que = input()
		answer = question_filler(que,doc_dict,topic_dict)
		print(">>", answer)
		answer = answer.split()
		if "goodbye" in answer:
			break
