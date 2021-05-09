def merge_sort(nums, start, end):
    if len(nums) > 1:
        middle = len(nums) // 2
        left = nums[:middle]
        right = nums[middle:]
        merge_sort(left, start, start + middle - 1)
        merge_sort(right, start + middle, end)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i+=1
            else:
                nums[k] = right[j]
                j+=1
            k+=1

        while i < len(left):
            nums[k] = left[i]
            i+=1
            k+=1

        while j < len(right):
            nums[k] = right[j]
            j+=1
            k+=1

        print(start, end, nums[0], nums[-1])

N=int(input())

p = input().split()[:N]
p = [int(x) for x in p]

merge_sort(p, 1, len(p))

print(*p)