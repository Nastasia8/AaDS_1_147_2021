def merge_sort(numbers):
    if len(numbers) <= 1:
        return numbers, 0
    middle = int( len(numbers) / 2 )
    left, a = merge_sort(numbers[:middle])
    right, b = merge_sort(numbers[middle:])
    result, c = internal_sort(left, right)
    return result, (a + b + c)

def internal_sort(left, right):
    result = []
    count = 0
    i, j = 0, 0
    left_len = len(left)
    while i < left_len and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += left_len - i
            j += 1
    result += left[i:]
    result += right[j:]
    return result, count

      
n = int(input())
numbers = list(map(int, input().split()))[:n]
print(merge_sort(numbers)[1])