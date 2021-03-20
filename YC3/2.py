def rotate(l, n):
    return l[-n:] + l[:-n]

counter = 0
S = list(input())
T = list(input())
for i in range(len(S)):
    S = rotate(S,0)
    if S == T:
        counter=i+1
if counter == 0:
    counter = -1
print(counter)
