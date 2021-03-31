# def psp(line):
#     open = "<({"
#     close = ">)}"
#     stack = []
#     p = 0
#     for i in line:
#         if (i in open):
#             if (stack == []):
#                 stack.append(open.index(i))
#             else:
#                 p = p  + 1   
#         elif i in close:
#             if stack and stack[-1] == close.index(i):
#                 stack.pop()
#             else:
#                 p = p + 1

#     return p

# def main():
#     text = "))((("
#     print(psp(text))

# main()    



def psp(line):
    open = "<({"
    close = ">)}"
    stack = []
    p = 0
    arr = list(line)
    for i, sims in enumerate(arr):
        if (sims in open):
            if ( arr[i] == arr[i-1]) and (arr[i]):
                p = p + 1
            else:
                 stack.append(open.index(sims))    

               
             
        elif sims in close:
            if stack and stack[-1] == close.index(sims):
                stack.pop()
            else:
                p = p + 1

    return p

def main():
    text = input()
    print(psp(text))

main()    

                


        
