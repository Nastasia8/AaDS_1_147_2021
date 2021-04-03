def CSS(a):
    a.replace(' ', '')
    stack = []*len(a)
    counter = 0
    for i in a:
        if i == '(':
            stack.append('(')
        if i == ')' and not stack:
            counter+=1
        elif i == ')' and stack:
            stack.pop()
        #print(counter)
        #print(stack)
    return len(stack)+counter


def main():
    a = input()
    print(CSS(a))

main()