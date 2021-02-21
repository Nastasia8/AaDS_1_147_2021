def counter(tuple, a):
    if a not in tuple:
        print("The tuple doesn't contain a character = ", a)
    if a in tuple:
        ind = 0
        first_ind = float("inf")
        last_ind = 0
        for i in tuple:
            ind += 1
            if a == i:
                last_ind = ind
                if first_ind > ind:
                    first_ind = ind
        if first_ind == last_ind:
            print(tuple[first_ind - 1:])
        else:
            print(tuple[first_ind - 1:last_ind])
        print(first_ind, last_ind)

a = int(input())
tuple = (1, 2, 3, 4, 5, 4, 6, 2, 4, 7, 9, 4, 5, 6, 5, 0, 4, 2)
counter(tuple, a)
