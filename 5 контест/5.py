from math import gcd 


def build(x1, x2, x3, x4, x5): #собираем наше деревцо
    if x3-x2 == 1:        
        x4[x1] = x5[x2]
        return
    p = (x2+x3)//2            
    build(2*x1 + 1, x2, p, x4, x5)
    build(2*x1 + 2, p, x3, x4, x5)
    x4[x1] = gcd(x4[2*x1 + 1], x4[2*x1 + 2])

def update(x1, x2, x3, x4, index, value): 
    if x3 - x2 == 1:    
        x4[x1] = value
        return
    middle = (x3+x2)//2  # Находим центр
    if index < middle:   # Если index меньше middle, то возвращается меньшее значение
        update(x1*2+1, x2, middle, x4, index, value)
    else:
        update(x1*2+2, middle, x3, x4, index, value)   #иначе действие обратное действию выше
    x4[x1] = gcd(x4[2*x1 + 1], x4[2*x1 + 2])  #NOD    

def get_nod(x1, x2, x3, x4, proz1, proz2): #получаем NOD
    if proz1 <= x2 and proz2 >= x3: 
        return x4[x1]
    if proz1 >= x3 or proz2 <= x2:  
        return 0
    p = (x2+x3)//2
    tl = get_nod(2*x1 + 1, x2, p, x4, proz1, proz2) 
    tr = get_nod(2*x1 + 2, p, x3, x4, proz1, proz2)
    return gcd(tl, tr)

def main():  
    n = int(input())  
    x4 = [0]*(4*n) 
    x5 = list(map(int, input().split()))[:n]  
    build(0, 0, n, x4, x5)
    q = int(input())
    res = []
    while q !=0:
        type_q, x2, x3 = map(str, input().split())
        if type_q == "s":
            res.append(get_nod(0, 0, n, x4, int(x2)-1, int(x3)))
        else:
            update(0, 0, n, x4, int(x2)-1, int(x3))
        q-=1
    print(*res) # *нужна здесь почему?  

main()  