#3.1
def Ira(q):
    Q=[0]*len(q)
    for m in range(len(q)-1):
        Y=Q[m]
        while Y>0 and q[m+1]!=q[Y]:
            Y=Q[Y-1]
        if q[m+1]==q[Y]:
            Q[m+1]=Y+1
        else:
            Q[m+1]=0
    return Q
def Pups():
    q=input()
    n=input()
    ennd=n+'&'+q
    Q=Ira(ennd)
    for m in range(len(Q)):
        if Q[m]==len(n):
            print(m-2*len(n),end=' ')
          
Pups()
#3.2
def Ira(m,n,am):
    Q = 0
    for i in range(len(m)):
        Q = (Q*n + ru(m[i]))%am
    return Q

def Pups(m,q,n,am):
    if m!= q:
        l = 1
        q = q[1:] + q[0]
        Q = Ira(m, n, am)
        pu = Ira(q, n, am)
        di = 1
        for i in range(len(m)-1):
            di = (di * n) %am
        for i in range(len(q)-1):
            if Q == pu:
                break
            else:
                pu=(n*(pu-ru(q[i])*di) + ru(q[i]))%am 
                l+= 1
        if Q == pu:
            print(l)
        else:
            print(-1)
    else:
        print(0)

def Kyst():
    m=input() 
    q=input() 
    n = 26
    am = 10 ** 9 + 7
    Pups(m, q, n, am)

Kyst()
#3.3
def Ira(Q):
    V=[0]*len(Q)
    for i in range(len(Q)-1):
        Z=V[i]
        while Z>0 and Q[i+1]!=Q[Z]:
            Z=V[Z-1]
        if Q[i+1]==Q[Z]:
            V[i+1]=Z+1
        else:
            V[i+1]=0
    return V
def Pups():
    Q=input()
    Q_t=Q+"&"+Q
    L=Ira(Q_t)
    Li=L[-1]-L[len(Q)-1] 
    V=len(Q)//Li
    if Q[:Li]*V==Q:
        print(V)
    else:
        print(1)
Pups()
#3.4
def Ira(Q,E):
    m=[0]*E
    for i in range(E-1):
        Y=m[i]
        while Y>0 and Q[i+1]!=Q[Y]:
            Y=m[Y-1]
        if Q[i+1]==Q[Y]:
            m[i+1]=Y+1
        else:
            m[i+1]=0
    return m
st = input()
Q = Ira(st,len(st))
print(len(st) - Q[len(Q)-1])