
Text="Hello hi how hello are and you I am fine thank you and you hello You Thank And"
dict={}
for word in Text:
    if word in dict:
        dict[word]+=1
    else:
        dict[word]=1
print(dict)   