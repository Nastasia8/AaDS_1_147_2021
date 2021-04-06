def sort(a):
    b = []*len(a)
    stack = [] * len(a)
    for i in range(0,len(a)):
        stack.append(a[i])
        if b:
            if b[i] > stack[-1]:
                b.append(stack.pop())
        else:
            b.append(stack.pop())
        print(stack)

def main():
    n = int(input())
    a = list(map(int,input().split()))[:n]
    
    sort(a)

main()