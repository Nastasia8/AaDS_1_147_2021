"""
>>> import io, sys 
>>> sys.stdin = io.StringIO(chr(10).join(['5','5','4','3','2','1']))  # input
>>> Function()
1 2 4 5
4 5 1 2
3 5 1 3
1 5 1 5
1 2 3 4 5 
"""


def Function():
    def mergeSort(Numbers_2, Numbers):

        if len(Numbers_2) > 1:
            mid = len(Numbers_2)//2
            lefthalf = Numbers_2[:mid]
            righthalf = Numbers_2[mid:]

            mergeSort(lefthalf, Numbers)
            mergeSort(righthalf, Numbers)

            i = 0
            j = 0
            k = 0
            while i < len(lefthalf) and j < len(righthalf):
                if lefthalf[i] < righthalf[j]:
                    Numbers_2[k] = lefthalf[i]
                    i = i+1
                else:
                    Numbers_2[k] = righthalf[j]
                    j = j+1
                k = k+1

            while i < len(lefthalf):
                Numbers_2[k] = lefthalf[i]
                i = i+1
                k = k+1

            while j < len(righthalf):
                Numbers_2[k] = righthalf[j]
                j = j+1
                k = k+1

            if Numbers.index(Numbers_2[-1])+1 > Numbers.index(Numbers_2[0])+1:
                print(Numbers.index(
                    Numbers_2[0])+1, Numbers.index(Numbers_2[-1])+1, Numbers_2[0], Numbers_2[-1])
            else:
                print(Numbers.index(
                    Numbers_2[-1])+1, Numbers.index(Numbers_2[0])+1, Numbers_2[0], Numbers_2[-1])

    Num = input()
    Numbers = list(map(int, input().split()))
    Numbers_2 = Numbers
    mergeSort(Numbers_2, Numbers)
    print(*Numbers_2)


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
