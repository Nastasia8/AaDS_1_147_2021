words=['Crime and Punishment', 1, 331, 1866, 'The Master and Margarita', 1, 470, 1966, 'War and Peace', 4, 1274, 1869, 'And Quiet Flows the Don', 4, 1600, 1940]
Dict={}
def Function(Dict,words):
    for word in words:
        if type(word)==str:
            wor=word
            Dict[wor]=[]
        else:
            Dict[wor].append(word)
    print(Dict)
    
Function(Dict,words)