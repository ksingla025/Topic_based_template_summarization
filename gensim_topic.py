from gensim import corpora
import tempfile, os, sys, glob
from gensim import corpora, models, similarities

from summarize_codes import *
from template import *



TEMP_FOLDER = "./model/"
print('Folder "{}" will be used to save temporary dictionary and corpus.'.format(TEMP_FOLDER))

document_folder = sys.argv[1]
files = glob.glob(document_folder+"/depth*")

documents = []
file_names = []
for file in files:
	print(file)
	file_names.append(os.path.basename(file))
	documents.append(uccfilereader(file))
print(documents[0])
print("#Total documents", len(documents))


#ocuments = ["thanks thanks .um so this is our you know first time together i'm uh really excited to be working with you and first of all just wanted to check in and see like how you're feeling about um you know this first counseling session .um so this is our you know first time together i'm uh really excited to be working with you and first of all just wanted to check in and see like how you're feeling about um you know this first counseling session .um so this is our you know first time together i'm uh really excited to be working with you and first of all just wanted to check in and see like how you're feeling about um you know this first counseling session .yeah you know i'm excited i guess it's something i've never really done before so .yeah you know i'm excited i guess it's something i've never really done before so .yeah .yeah 'cause so uh a little bit about kind of my family history my so my mom and my sister both suffer from anxiety .yeah 'cause so uh a little bit about kind of my family history my so my mom and my sister both suffer from anxiety .um and i started taking uh lexapro uh let's see i'm probably day twelve or something .okay well that's great that you are you know able to recognize what's going on and take you know this step to um start working toward you know getting some support with that both in the medication and then coming here as well .so this being you know the first one i am really interested in getting to know more you know about you um so getting to know who you are getting to know um a bit about you mentioned some anxiety uh you know sort of the predominant reason for coming in and so a bit more about your experiences with anxiety um you know some of your history with it what it's looking like for you right now um things that you've tried to do to you know cope with it or manage it um and then discuss some of your goals as well and i also wanted to see if there's anything that you wanted to make sure we discussed today as well .anything that you're like oh i want to make sure you know we get to that .okay yeah and well maybe at the end so at the end we'll you know debrief and process everything especially being you know this is our first session and your first time in therapy in general um i really like to adapt therapy to each person so um you know there's no offense in tinkering around in response to what may work really well for you or what might not work as well one other thing i just want to let you know before we jump in too is i'm a psychology phd student so what that means is i'm in the process of becoming a psychologist and am not yet a licensed psychologist so i'm working under the supervision of one of our psychologists here at the counseling center doctor [SUPERVISOR] .okay um yeah so i'm a first year phd student here too um in econ department um so i just finished undergrad in may um and not here so moved to salt lake in july so i've been here since then um and yeah it's just kind of been uh an interesting transition because you know throughout high school i always had you know really strong kind of group of friends and then same in college um and then you know all of a sudden coming here where i don't really know anyone ^ .okay um yeah so i'm a first year phd student here too um in econ department um so i just finished undergrad in may um and not here so moved to salt lake in july so i've been here since then um and yeah it's just kind of been uh an interesting transition because you know throughout high school i always had you know really strong kind of group of friends and then same in college um and then you know all of a sudden coming here where i don't really know anyone ^ .i mean it's definitely the you know being scared of failure or the trajectory of my life you know so like in column one is like if i you know for example if i have had sex in the past like couple weeks or something you know and i'll be like oh my god like if she gets pregnant like i'm gonna have to drop out of school [nvv] my life will go down a horrible path you know and so it's kind of like stress like that of what the future you know what's gonna happen in the future and stuff like that so that's kind of like i guess kind of what yeah in general my anxiety's about i don't really have social anxiety although it's gotten a little worse just kind of being in a new place but in general i feel like i'm pretty apt at dealing with situations and i generally make friends pretty easily but yeah .i mean it's definitely the you know being scared of failure or the trajectory of my life you know so like in column one is like if i you know for example if i have had sex in the past like couple weeks or something you know and i'll be like oh my god like if she gets pregnant like i'm gonna have to drop out of school [nvv] my life will go down a horrible path you know and so it's kind of like stress like that of what the future you know what's gonna happen in the future and stuff like that so that's kind of like i guess kind of what yeah in general my anxiety's about i don't really have social anxiety although it's gotten a little worse just kind of being in a new place but in general i feel like i'm pretty apt at dealing with situations and i generally make friends pretty easily but yeah .okay try not to think about a pink elephant what are you thinking about right now .um well you know exercise is big .um well you know exercise is big .yeah it's like exercise things that might distract yourself .that's a great thing to recognize that really like being around other people is helpful .um so i do like to you know build off of what already has worked for you if there is if there are things that you like oh that's just been really helpful and i just don't do it anymore or things like that um as far as other things i'll say that with anxiety you know each person is different and what works well for you might you know somebody else might not find helpful and what somebody else finds helpful um might not be helpful for you um like you mentioned like you said you have mixed feelings about mindfulness for example and so that's like a perfect example of something that some people really love and they're like this is what grounds me and other people are like i hate this and you know every gradient in between um and so um one of the things we can do is um explore you know um some different things and have opportunities for you to test things out i have somewhere i think it's uh buried down here or no my [du] a bit of a mess right now but i have a sheet about swear i had a bunch of these of this um here we go um so this might be one place to start is this worksheet on so this was a list of possible ways to um shift attention away when um you know you are feeling anxious um all uh but i don't want to um well sometimes it can be helpful to really you know acknowledge that emotion and to sit with it um and my goal or my where i'm coming from as a clinician is not necessarily to be like you shouldn't we don't want you to ever feel anxiety or anything like that um but these might this might be a place to start for things you can do when you are feeling anxiety to help you manage that emotion um i'm wondering you know as you look at this is there anything that um stands out to you that you're like oh yeah i might like to do that .all right well shall we schedule a next session .uh sure yeah",
#			 "okay .how are you this morning .uh okay  .just okay .yeah well i'm glad that you're here .yeah well i'm glad that you're here .makes it more comfortable to sit .yeah .yeah so today um it's really for me to get to know like you what's been going on and then we can start thinking about like where to go from here how do you feel about that .yeah feel free to ask any questions along the way .yeah and um um so i moved here three years ago and um i always i always felt a lot of anxiety but was growing in a small village was like a small thing so uh we don't talk about those things 'cause it's not important and then uh then after i got i got married and i feel that i'm having more anxiety and more stress and in this marriage also i'm constantly angry and arguing and the stuff so but so now i'm gonna cry [laughs] .yeah and um um so i moved here three years ago and um i always i always felt a lot of anxiety but was growing in a small village was like a small thing so uh we don't talk about those things 'cause it's not important and then uh then after i got i got married and i feel that i'm having more anxiety and more stress and in this marriage also i'm constantly angry and arguing and the stuff so but so now i'm gonna cry [laughs] .yeah and um um so i moved here three years ago and um i always i always felt a lot of anxiety but was growing in a small village was like a small thing so uh we don't talk about those things 'cause it's not important and then uh then after i got i got married and i feel that i'm having more anxiety and more stress and in this marriage also i'm constantly angry and arguing and the stuff so but so now i'm gonna cry [laughs] .[crying] because i don't know why i'm so angry all the time and anxious and i can't do my homework and i'm i have a paper was due monday and i did on sunday night and i i supposed to have i had a paper yesterday i did yesterday morning i have a video essay due tomorrow i even didn't start it and i'm and i know that everything's inside my mind because my husband is he's great but i don't know why i i'm constantly angry and i fight with him but he's but he never fight back so and then i feel guilty and he understand and but so [laughs] [du] but and now and um so yeah [laughs] .okay your first semester .okay and then we i work in a a restaurant on weekends and i get i get very stressed over there 'cause working a restaurant you know working with food with people work with um people with [du] stuff and so i get at home very angry sometimes and uh when i'm angry i want to be i want to be quiet i want to get home and not talk to anybody just sit and watch t v and [PATIENT PARTNER] wants to talk about my feelings and i don't want to and but but he keep asking me why i don't want to talk about it and then i get angry and we start discussing and um so oh i where we what is the question i got lost [laughs] .mm okay um um since i was uh [nvv] another thing for you to know is that uh when i was a kid i was i was sexual abused .yeah it's [du] ^ .yeah so i'm like i have any feelings about this but and um so i so growing up i was i became very sexual and um i started to have not boyfriends but like affairs when i was like ten eleven and um and this and i'm talking about they the nineties so in the nineties in my small village it was rural ^2 .yeah and um so so a way to deal with anxiety i think was through masturbation and uh i started doing very young and i have never had a time where i stopped and um i know that also i use masturbation a lot to deal with anxiety and at the end i don't do my homework i don't do anything i spend five six hours watch porn and then i do everything um like one day before it's due .because um himself he he so he had depression and during school also he was in uh in a mormon family so he had therapy to deal with his homosexuality and and helped him so so so he taught me that maybe it could help me so .because um himself he he so he had depression and during school also he was in uh in a mormon family so he had therapy to deal with his homosexuality and and helped him so so so he taught me that maybe it could help me so .yes .yeah yeah so uh maybe uh next time we se each other you can think about um noticing uh when you do get angry like what triggers that and what um how do you feel inside what are some of the things that go in your head as you start building up like when you're starting to get anxious really anxious and then angry what are your thoughts and how are you feeling during that time how do is that something that you feel like you can do .yeah this is something you've been holding on for a long time and it's affecting a lot of things and i hope that i can support you and um help you through all this this stressful time that you're experiencing um i usually see uh folks every two weeks is that something that you feel like you can do be okay .no i i think yeah .yes so nice to meet you and i'm glad that you know you came in and really opened yourself up to me like i feel really honored that you shared some of that sounds like you haven't shared with a lot of people"]
# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
         for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1] for text in texts]

from pprint import pprint  # pretty-printer
pprint(texts)


dictionary = corpora.Dictionary(texts)
dictionary.save(os.path.join(TEMP_FOLDER, 'deerwester.dict'))  # store the dictionary, for future reference
print(dictionary)
dictionary.save_as_text(TEMP_FOLDER+"dictionary.txt")


print(dictionary.token2id)
corpus = [dictionary.doc2bow(text) for text in texts]


print(dictionary[0])
print(dictionary[1])
print(dictionary[2])

tfidf = models.TfidfModel(corpus) # step 1 -- initialize a model
tfidf.save(TEMP_FOLDER+"model.tfidf")

doc_bow = [(0, 1), (1, 1)]
#print(tfidf[doc_bow]) # step 2 -- use the model to transform vectors


corpus_tfidf = tfidf[corpus]
#for doc in corpus_tfidf:
#    print(doc)


lsi = models.LsiModel(corpus_tfidf, id2word=dictionary, num_topics=100) # initialize an LSI transformation
lsi.save(TEMP_FOLDER+"model.lsi")

#print(corpus_lsi)
print("Topics\n")
#print(lsi.get_topics().shape)

topic_dict = {}
for i in range(0,100):
#   p = lsi.print_topic(i, topn=20)
    topic_dict[i] = dict(lsi.show_topic(i, topn=40)).keys()



corpus_lsi = lsi[corpus_tfidf] # create a double wrapper over the original corpus: bow->tfidf->fold-in-lsi




#	print("Topic "+str(i), dict(lsi.show_topic(i, topn=30)))

print("separator")
i = -1
for doc in corpus_lsi: # both bow->tfidf and tfidf->lsi transformations are actually executed here, on the fly
    i = i +1
    print("---------------------------------------------------------")
    print(file_names[i])
    doc_dict = dict(doc)
    doc_keys_sorted = sorted(doc_dict, key=lambda d: abs(doc_dict[d]))[-8:]
    print(template1(doc_keys_sorted,topic_dict))
    print(template2(doc_keys_sorted,topic_dict))
    print(template3(doc_keys_sorted,topic_dict))
#   	print(doc_keys_sorted)

