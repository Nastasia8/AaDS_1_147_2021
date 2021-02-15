text = 'Hello hi how hello are and you I am fine thank you and you hello You Thank And'.lower().split(' ')
dict = {}
for word in text:
#     if word in dict:
#         dict[word]+=1
#     else:
#         dict[word]=1
    dict[word]=dict.get(word,0)+1
print(dict)          