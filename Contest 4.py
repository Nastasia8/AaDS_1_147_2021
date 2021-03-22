def merge_sort(Numbers_2, Count):

    if len(Numbers_2) > 1:
        mid = len(Numbers_2)//2
        left = Numbers_2[:mid]
        right = Numbers_2[mid:]
        Count = merge_sort(left, Count)
        Count = merge_sort(right, Count)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Numbers_2[k] = left[i]
                i += 1
            else:
                Numbers_2[k] = right[j]
                j = j+1
                Count += len(left)-i
            k = k+1
        while i < len(left):
            Numbers_2[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            Numbers_2[k] = right[j]
            j = j+1
            k = k+1

    return Count


Count = 0
Num = int(input())
Numbers = list(map(int, input().split()))[:Num]
Count = merge_sort(Numbers, Count)
print(Count)
