#!/usr/bin/python

def question_filler(text,doc_dict,topic_dict):

	doc_keys_sorted = sorted(doc_dict, key=lambda d: abs(doc_dict[d]))[-8:]	
	text = text.lower().split()

	if "problems" in text or "problem" in text:
		return template2(doc_keys_sorted,topic_dict)
	if "symptoms" in text or "symptom" in text:
		return template1(doc_keys_sorted,topic_dict)
	if "about" in text or "topic" in text:
		return template3(doc_keys_sorted,topic_dict)
	if "bye" in text or "goodbye" in text or "bye" in text:
		return "Please feel free to comeback. goodbye"
	else:
		return "I am not sure. Ask me about problems, symptoms, about :/"
	


symptoms = ['itching', 'danger-to-others', 'obsessive-behavior', 'tremors', 'hypersomnia', 'academic-failure',\
			'enuresis', 'headache', 'sexual-dysfunction', 'suicidal-ideation', 'anger', 'inattentiveness',\
			'phantom-pain', 'delusions', 'apnea', 'sweating', 'guilt', 'rash', 'anxiety', 'back-pain',\
			'moodiness', 'danger-to-self', 'hallucinations', 'restlessness', 'low-self-esteem', 'isolation',\
			'detached-behavior', 'crying', 'sadness', 'acting-out', 'alopecia', 'compulsive-behavior', 'apathy',\
			'withdrawn', 'disorganized-thoughts', 'impulsivity', 'insomnia', 'vertigo', 'fantasizing', 'dysphagia',\
			'loss-of-appetite', 'anhedonia', 'deceitfulness', 'paranoia', 'seizures', 'nausea', 'resentment',\
			'confusion', 'indecisiveness', 'general-pain', 'exhaustion', 'severe-sensitivity', 'depression',\
			'fainting', 'stuttering', 'fearfulness', 'encopresis', 'dreams', 'chronic-pain', 'irritability', \
			'suspiciousness', 'fatigue', 'despair', 'withdrawal-sickness', 'aggression', 'social-inhibition',\
			'panic', 'mania', 'problems-concentrating', 'vomiting', 'hyperactivity', 'racing-thoughts',\
			'nightmares', 'suicidal-behavior', 'dysphoria', 'avoidance', 'hyperphagia', 'cutting']


problems = ['drinking','drugs','bad-grades', 'family-pressure', 'smoking']

about = ""
about = ['family-issues','fight', 'fights','family-history']

def template1(doc_topics,topic_word_dict):
	'''
	symptoms
	'''
	text = "Patient shows symptoms of "

	symptoms_o = []
	for symptom in symptoms:

		for topic in doc_topics:
			for word in topic_word_dict[topic]:

				if word == symptom:
					symptoms_o.append(word)

	symptoms_o = list(set(symptoms_o))
	if symptoms_o != []:
		text = text + ",".join(symptoms_o)
	else:
		text = "NO symtoms found"

	return text

def template2(doc_topics,topic_word_dict):
	'''
	symptoms
	'''
	text = "Patient reports that he/she do "

	symptoms_o = []
	for symptom in problems:

		for topic in doc_topics:
			for word in topic_word_dict[topic]:

				if word == symptom:
					symptoms_o.append(word)

	symptoms_o = list(set(symptoms_o))
	if symptoms_o != []:
		text = text + ",".join(symptoms_o)
	else:
		text = "NO problem found"

	return text

def template3(doc_topics,topic_word_dict):
	'''
	symptoms
	'''
	text = "Also talks about "

	symptoms_o = []
	for symptom in about:

		for topic in doc_topics:
			for word in topic_word_dict[topic]:

				if word == symptom:
					symptoms_o.append(word)

	symptoms_o = list(set(symptoms_o))
	if symptoms_o != []:
		text = text + ",".join(symptoms_o)
	else:
		text = "NO talk about"

	return text

'''
def template2(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):


def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):

def template1(topics,document_topic_weights):


def template1(topics,document_topic_weights):


def template1(topics,document_topic_weights):
'''