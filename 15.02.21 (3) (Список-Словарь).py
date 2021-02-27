def func():
    words=['Crime and Punishment', 1, 331, 1866, 'The Master and Margarita', 1, 470, 1966, 'War and Peace', 4, 1274, 1869, 'And Quiet Flows the Don', 4, 1600, 1940]
    dict={}
    stroka=''
    for word in words:
        if (type(word)==str):
            dict[word]=[]
            stroka=word
        else:
            dict[stroka].append(word)
    return (dict)
print (func())
