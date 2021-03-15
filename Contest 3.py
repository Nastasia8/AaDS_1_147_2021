
def merge_sort(Numbers_2, Numbers):

    if len(Numbers_2) > 1:
        mid = len(Numbers_2)//2
        left = Numbers_2[:mid]
        right = Numbers_2[mid:]

        merge_sort(left, Numbers)
        merge_sort(right, Numbers)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                Numbers_2[k] = left[i]
                i = i+1
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

        i = 1
        max_index = Numbers.index(Numbers_2[0])
        min_index = Numbers.index(Numbers_2[0])
        while i < len(Numbers_2):
            a = Numbers.index(Numbers_2[i])
            if max_index < a:
                max_index = a

            if min_index > a:
                min_index = a
            i += 1

        print(min_index+1, max_index+1, Numbers_2[0], Numbers_2[-1])


Num = input()
Numbers = list(map(int, input().split()))
Numbers_2 = Numbers
merge_sort(Numbers_2, Numbers)
print(*Numbers_2)
