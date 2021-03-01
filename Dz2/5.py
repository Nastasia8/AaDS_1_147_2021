text="Hello hi how hello are and you I am fine thank you and you hello You Thank And"
dict={}
for a in text.lower().split():
    if a in dict:
        dict[a]+=1
    else:
        dict[a]=1
print(dict)