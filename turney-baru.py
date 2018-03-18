import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# stop_words = set(stopwords.words("english"))
file = open("Apex-AD2600-Progressive-scan-DVD-player.txt","r")
process_text = file.read() #Membaca isi file
ex_text = sent_tokenize(process_text) #Mentokenisasi isi dari variabel process_text


# # --- STOPWORDS ---
# filtered_sentence = []
# for t in train_text:
#     if t not in stop_words:
#         filtered_sentence.append(t)

#--- Speech tagging --- ( Melakukan speech tagging untuk setiap kata pada setiap kalimat dan melakukan identifikasi rule turney)
def process_content():
    try:
        for i in ex_text:
            words = word_tokenize(i)
            tagged = pos_tag(words)
            chunkGram = r"""
                Rule 1: {<JJ>(<NN>|<NNS>)}
                Rule 2: {(<RB>|<RBR>|<RBS>)<JJ>}
                Rule 3: {<JJ><JJ>}
                Rule 4: {(<NN>|<NNS>)<JJ>}
                Rule 5: {(<RB>|<RBR>|<RBS>)(<VB>|<VBD>|<VBN>|<VBG>)}
                """
            chunkParser = nltk.RegexpParser(chunkGram)
            chunked = chunkParser.parse(tagged)
            # print(chunked)
            # print(tagged)
            # for subtree in chunked.subtrees(filter=lambda t: t.label() == 'Rule 1'):
            #     print(subtree)
            for subtree in chunked.subtrees():
                if subtree.label() == "Rule 1":
                    print("Sentence : " + i)
                    print("Rule 1: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 2":
                    print("Sentence : " + i)
                    print("Rule 2: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 3":
                    print("Sentence : " + i)
                    print("Rule 3: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 4":
                    print("Sentence : " + i)
                    print("Rule 4: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 5":
                    print("Sentence : " + i)
                    print("Rule 5: " + str(subtree.leaves()))
                    print("")
    except exception as e:
        print("gagal")

process_content()