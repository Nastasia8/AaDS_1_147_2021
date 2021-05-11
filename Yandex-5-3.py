# 1 вариант
# TL
def find(section):
    a = min(section)
    while a > 0:
        for i in range(len(section)):
            if section[i] % a != 0:
                a -= 1
                break
        break
    return a


result = []
n = int(input())
array = list(map(int, str(input()).split()[:n]))
for i in range(int(input())):
    a = str(input()).split()[:2]
    section = array[int(a[0]) - 1:int(a[1])]
    result.append(str(find(section)))
print(" ".join(result))

# 2 вариант
# WA


def find(section):
    while len(section) != 1:
        a = section.pop(0)
        b = section.pop(0)
        while b != 0:
            a, b = b, a % b
        section.insert(0, a)
    return section[0]


result = []
n = int(input())
array = list(map(int, str(input()).split()[:n]))
k = int(input())
for i in range(k):
    a = str(input()).split()[:2]
    result.append(str(find(array[int(a[0]) - 1:int(a[1])])))
print(" ".join(result))
