Numbers = [5, 4, 3, 2, 1]


def mergeSort(alist):

    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1
        if Numbers.index(alist[-1])+1 > Numbers.index(alist[0])+1:
            print(Numbers.index(
                alist[0])+1, Numbers.index(alist[-1])+1, alist[0], alist[-1])
        else:
            print(Numbers.index(alist[-1])+1,
                  Numbers.index(alist[0])+1, alist[0], alist[-1])


alist = Numbers
mergeSort(alist)
print(*alist)
