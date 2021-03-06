import nltk
from nltk import word_tokenize, pos_tag, sent_tokenize, PunktSentenceTokenizer
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

# stop_words = set(stopwords.words("english"))
file = open("Apex-AD2600-Progressive-scan-DVD-player.txt","r")
process_text = file.read() #Membaca isi file
ex_text = sent_tokenize(process_text) #Mentokenisasi isi dari variabel process_text

true_words = []
wrong_words = []
no_pattern = []

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
            for subtree in chunked.subtrees():
                if subtree.label() == "Rule 1":
                    aspek = []
                    true_words.append(str(subtree.leaves()))
                    print("Sentence : " + i)
                    print("Rule 1: " + str(subtree.leaves()))
                    noun_phrases_list = [' '.join(leaf[0] for leaf in subtree.leaves())
                      for tree in chunkParser.parse(tagged).subtrees()]
                    aspek.append(noun_phrases_list[0])
                    precision(i,aspek)
                    print("")
                elif  subtree.label() == "Rule 2":
                    wrong_words.append(str(subtree.leaves()))
                    print("Sentence : " + i)
                    print("Rule 2: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 3":
                    wrong_words.append(str(subtree.leaves()))
                    print("Sentence : " + i)
                    print("Rule 3: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 4":
                    true_words.append(str(subtree.leaves()))
                    print("Sentence : " + i)
                    print("Rule 4: " + str(subtree.leaves()))
                    print("")
                elif  subtree.label() == "Rule 5":
                    wrong_words.append(str(subtree.leaves()))
                    print("Sentence : " + i)
                    print("Rule 5: " + str(subtree.leaves()))
                    print("")
        benar = len(true_words)
        salah = len(wrong_words)
        extraction_word = 431
        Precision = (benar / (benar + salah))*100
        print("Precision : " "%0.2f" % Precision,"%")
        Recall = (benar / extraction_word )*100
        print("Recall : " "%0.2f" % Recall)
    except exception as e:
        print("gagal")

def precision(i,aspek):
    kalimat = i
    hasil = []
    kata = []
    str = i
    for i in range(0, len(str)):
        if (str[i] == '#'):
            sen = ''.join(hasil)
            # text = ''.join([char for char in sen if char.isalpha()])
            kata.append(sen)
            break
            # print(str[i])
        elif str[i] in ('[' ,'+' ,'-',']','1','2','3'):
            str.replace("[", "").replace("+", "").replace("-", "").replace("]", "").replace("1","").replace("2","").replace("3","")
        elif (str[i] != ','):
            hasil.append(str[i])
        elif (str[i] == ','):
            sen = ''.join(hasil)
            # text = ''.join([char for char in sen if char.isalpha()])
            kata.append(sen)
            hasil = []

    print("Aspek sebenarnya : " , kata)
    print("Aspek yang terekstrasi : " , aspek)


    if ( i != kalimat):
        benar = 0
        salah = 0
        if( kata == aspek):
            benar = benar +1
            prec = (benar / ( benar + salah))*100
            print("a")
            print("Precision : ",prec)
        else:
            benar = benar + 0
            salah = 1
            prec = (benar / (benar + salah)) * 100
            print("b")
            print("Precision : ",prec)
    else:
        kalimat = i
        if ( kata ==  aspek ):
            benar = benar + 1
            prec = (benar / (benar + salah)) * 100
            print("c")
            print("Precision : ", prec)
        else:
            benar = benar + 0
            salah = 1
            prec = (benar / (benar + salah)) * 100
            print("d")
            print("Precision : ", prec)


process_content()