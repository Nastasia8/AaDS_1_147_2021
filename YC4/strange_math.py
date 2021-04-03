def main():
    s = input().replace(' ','')
    stack = []
    for i in s:
        if i.isnumeric():
            stack.append(int(i))
        else:
            d2 = stack.pop()
            d1 = stack.pop()
            if i == '+':
                stack.append(d1 + d2)
            elif i == '*':
               stack.append(d1 * d2)
            elif i == '-':
                stack.append(d1 - d2)
    print(stack.pop())

main()