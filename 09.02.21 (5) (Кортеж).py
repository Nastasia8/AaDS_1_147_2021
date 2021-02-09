text='Hello hi how hello are and you I am fine thank you and you hello You Thank And'.lower()
dictionary={}
for word in text.split(' '):
    if word in dictionary:
        dictionary[word]+=1
    else:
        dictionary[word]=1
print (dictionary)
#2 способ
text='Hello hi how hello are and you I am fine thank you and you hello You Thank And'.lower()
dictionary={}
for word in text.split(' '):
    dictionary[word]=dictionary.get(word,0)+1
print (dictionary)
