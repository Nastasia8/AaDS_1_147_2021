def sort(vvod, vvod_A, vvod_B):
    stack = []
    i = 1
    j = 1
    for number in vvod_A:
        if number != i:
            stack.append(number)
            continue
        vvod_B.append(number)
        i += 1
        for j in range(len(stack)):
            if stack[-1] == i:
                vvod_B.append(i)
                stack.pop()
                i += 1
    if vvod_B[-1] == int(vvod):
        print("YES")
    else:
        print("NO")

def main():
        
    vvod = input()
    vvod_A = list(map(int, input().split()))
    vvod_B = []
    sort(vvod, vvod_A, vvod_B)       

main()