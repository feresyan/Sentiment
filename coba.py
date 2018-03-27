
hasil= []
kata = []
str = 'i/p button[+2]##im a more happier person after discovering the i/p button !'
for i in range(0, len(str)):
    if (str[i] == '#'):
        sen = ''.join(hasil)
        # text = ''.join([char for char in sen if char.isalpha()])
        kata.append(sen)
        break
        # print(str[i])
    elif str[i] in ('[' ,'+' ,'-',']','1','2','3'):
        str.replace("[","").replace("+","").replace("-","").replace("]","").replace("1","").replace("2","").replace("3","")
    elif (str[i] != ','):
        hasil.append(str[i])
    elif (str[i] == ','):
        sen = ''.join(hasil)
        # text = ''.join([char for char in sen if char.isalpha()])
        kata.append(sen)
        hasil = []

print(kata)
print(len(kata))
