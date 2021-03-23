def enter():
    n = int(input())
    if n < 1 or n > 1000:
        return(0)
    s = []
    for i in range(0, n):
        s.append(input())
        length = len(str(s[0]))
        if len(s[i]) != length or length > 20 or int(s[i]) < 0:
            return(0)
    print('Initial array:')
    print(*s, sep = ', ')
    func(length, s)

def func(length, s):
    rang = 10
    for i in range(length):
        print('**********\nPhase', i+1)
        m = [[] for k in range(rang)]
        for j in s:
            mesto = int(j) // 10 ** i % 10
            m[mesto].append(j)
        for k in range(len(m)):
            if not m[k]:
                print ('Bucket ' + str(k) + ': empty')
            else:
                print('Bucket ' + str(k) + ': ', end = '')
                print(*m[k], sep = ', ')
        s = []
        for t in range(rang):
            s = s + m[t]
    print('**********\nSorted array:')
    print(*s, sep = ', ')
        
enter()
