#sort 1
N = int(input())
numbers = [int(i) for i in input().split()][:N]

check = 0

for i in range(N-1):
    for j in range(N-i-1):
	    if numbers[j] > numbers[j+1]:
		    numbers[j],numbers[j+1] = numbers[j+1],numbers[j]
		    print(" ".join(map(str, numbers)))
		    check = 1
    
if check == 0:
	print(0)
	
#sort 2
N = int(input())
a = []

for i in range(N):
    a.append([int(j) for j in input().split()][:N])

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] > a[j][1]:
            a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)-1):
    for j in range(len(a)-i-1):
        if a[j+1][1] == a[j][1]:
            if a[j+1][0] < a[j][0]:
                a[j+1],a[j] = a[j],a[j+1]

for i in range(len(a)):
    print(*a[i])

#sort 3
N = int(input())
numbers = [int(i) for i in input().split()][:N]

def merge_two_lists(left, right):
    a = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            a.append(left[i])
            i += 1
        else:
            a.append(right[j])
            j += 1
            
    if i < len(left):
        a += left[i:]
    if j < len(right):
        a += right[j:]

    index_left = i + 1
    index_left_value = a[i]

    index_right = j + 1
    index_right_value = a[j]

    print(index_left, index_right, index_left_value, index_right_value)
    
    return a

def merge_sort(numbers):
    if len(numbers) == 1:
        return numbers

    middle = len(numbers)//2
    left = merge_sort(numbers[:middle])
    right = merge_sort(numbers[middle:])
    return merge_two_lists(left, right)

print(*merge_sort(numbers))

#sort 4

def main():
     n = int(input())
     array = list(map(int,input().split()))
     print (count_inversion(array))


def count_inversion(lst):
    return merge_count_inversion(lst)[1]

def merge_count_inversion(lst):
    if len(lst) <= 1:
        return lst, 0
    middle = int( len(lst) / 2 )
    left, a = merge_count_inversion(lst[:middle])
    right, b = merge_count_inversion(lst[middle:])
    result, c = merge_count_split_inversion(left, right)
    return result, (a + b + c)

def merge_count_split_inversion(left, right):
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
main()

#sort 5

N = int(input())

numbers = [int(i) for i in input().split()][:N]

print(len(set(numbers)))

