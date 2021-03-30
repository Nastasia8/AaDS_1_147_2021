n = input()
Line_A = list(map(int, input().split()))
Line_B = []
stack = []
i = 1
for number in Line_A:
    if number != i:
        stack.append(number)
        continue
    Line_B.append(number)
    i += 1
    for z in range(len(stack)):
        if stack[-1] == i:
            Line_B.append(i)
            stack.pop()
            i += 1
if Line_B[-1] == int(n):
    print("YES")
else:
    print("NO")
