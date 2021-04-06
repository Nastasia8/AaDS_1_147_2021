from collections import deque

def game(first, second):
    f_deck = deque(first)
    s_deck = deque(second)

    turns = 0
    while turns < 1e6 and (len(f_deck)*len(s_deck)):
        f_card = f_deck.popleft()
        s_card = s_deck.popleft()
        if f_card > s_card or (f_card == 0 and s_card == 9) :
            f_deck.append(f_card)
            f_deck.append(s_card)
        else:
            s_deck.append(f_card)
            s_deck.append(s_card)

        turns+=1


    if not f_deck:
        print("first", turns)

    elif not s_deck:
        print("second", turns)

    else:
        print("botva")

def main():
    first = list(map(int, input().split()))
    second = list(map(int, input().split()))

    game(first,second)
main()