def psp(line):
    stack = []
    p = 0
    for i in range(len(line)):
        if line[i] == "(":
            stack.append(line[i])
        else:
            if stack:
                stack.pop()
                p = p + 1
    return p

def main():
    text = input()
    print(len(text) - 2*psp(text))

main()
