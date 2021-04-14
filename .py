Tag = ["x", "3", "4", "5", "a", "d"]  # list(input())
char = Char = Tag[0]+Tag[4]+Tag[5]
tags = []
Num = Tag[1:4]
for i in range(5):
    if char != Char or i == 0:
        for j in range(3):
            Num = Num[1]+Num[2]+Num[0]
            tags.append(str(char[0]+str(Num)+char[1]+char[2]))
            tags.append(str(char[0]+str(Num)+char[2]+char[1]))
    char = char[1]+char[2]+char[0]
tags = set(tags)
print(len(tags))
print(*tags)
