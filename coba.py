
hasil= []
kata = []
str = 'look[+3],panel button layout[+3],feature[+2]##its very sleek looking with a very good front panel button layout , and it has a great feature set . '
for i in range(0, len(str)):
    if (str[i] == '#'):
        sen = ''.join(hasil)
        text = ''.join([char for char in sen if char.isalpha()])
        kata.append(text)
        break
        # print(str[i])
    elif str[i] in ('[' ,'+' ,'-',']'):
        str.replace("[","").replace("+","").replace("-","").replace("]","")
    elif (str[i] != ','):
        hasil.append(str[i])
    elif (str[i] == ','):
        sen = ''.join(hasil)
        text = ''.join([char for char in sen if char.isalpha()])
        kata.append(text)
        hasil = []

print(kata)
print(len(kata))
