def main():
    kor()
    
def kor():
    a = (1, 2, 2, 3, 1, 2, 4, 3, 2, 2)
    res = []
    i = 0
    y = 0
    while i < len(a):
        
        
        if a[i] == 2:
             res.insert(y, i)
            
            
        
        y += 1
    i += 1
    print(res)

main()


