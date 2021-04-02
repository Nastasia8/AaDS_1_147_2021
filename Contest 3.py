
def merge_sort(Numbers_2, start, end):

    if len(Numbers_2) > 1:
        mid = len(Numbers_2)//2
        left = Numbers_2[:mid]
        right = Numbers_2[mid:]
        merge_sort(left, start, start+mid-1)
        merge_sort(right, start+mid, end)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Numbers_2[k] = left[i]
                i += 1
            else:
                Numbers_2[k] = right[j]
                j = j+1
            k = k+1
        while i < len(left):
            Numbers_2[k] = left[i]
            i = i+1
            k = k+1
        while j < len(right):
            Numbers_2[k] = right[j]
            j = j+1
            k = k+1
        print(start, end, Numbers_2[0], Numbers_2[-1])


Num = int(input())
Numbers = list(map(int, input().split()))[:Num]
merge_sort(Numbers, 1, len(Numbers))
print(*Numbers)
