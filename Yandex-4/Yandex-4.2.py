# l = int(input())
# s = list(map(int, input().split()))

# stop = [] 
# road2 = [] 
# for i in range(l):
#     if s[i] > 1:
#         while len(road2) != 0 and s[i] == road2[-1] + 1:
#             road2.append(s[i])
#             continue
#         else:
#             stop.append(s[i])
#             continue
#     elif s[i] == 1:
#         road2.append(s[i])

# stop.reverse()
# road2 += stop

# if sorted(road2) == road2:
#     print('YES')
# else:
#     print('NO')

# l = int(input())
# s = list(map(int, input().split()))
 
# stop = [0] 
# road2 = [0] 
 
# for i in range(l):
#     while stop[-1] == road2[-1] + 1:
#         road2.append(tup[-1])
#         stop.pop()
#     if s[i] == road2[-1] + 1:
#         road2.append(s[i])
#     else:
#         stop.append(s[i])
 
# while stop[-1] == road2[-1] + 1:
#     road2.append(stop[-1])
#     stop.pop()
 
# if road2[-1] == l:
#     print('YES')
# else:
#     print('NO')

