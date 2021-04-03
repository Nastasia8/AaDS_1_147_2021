from collections import deque

first = deque(list(map(int, input().split())))
second = deque(list(map(int, input().split())))

k = 0
while k < 1e6 and (len(first)*len(second)):
    first_card = first.popleft()
    second_card = second.popleft()
    
    if first_card == 0 and second_card == 9:
        first.append(first_card)
        first.append(second_card)
    
    elif first_card == 9 and second_card == 0:
        second.append(first_card)
        second.append(second_card)    
    
    elif first_card > second_card:
        first.append(first_card)
        first.append(second_card)
    
    else:
        second.append(first_card)
        second.append(second_card)
    k += 1

if not first:
    print('second', k)
elif not second:
    print('first', k)
else:
    print('botva')